import sqlite3
import os
import discord
import random
from imageBuilder import *
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
from datetime import datetime, timedelta
from sqlEconomy import sqlEcoTimer
from embedBuilder import embedBuilder
from dictionaries import bankImgDic
import tempfile
import time
load_dotenv()

database = os.getenv("DB_PATH")
connection = sqlite3.connect(database)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, bankAmt INTEGER, dailyTimer TEXT)")


"""def userImgInfo(name, amount):
    width, height = 680, 100
    bgColor = (0,0,0)
    image = Image.new("RGB", (width, height), bgColor)
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("assets/fonts/LEMONMILK-Bold.otf", 32)
    except IOError:
        font = ImageFont.load_default()
    text_color = (255,255,255)
    text_margin = 20
    text_width1, text_height1 = draw.textsize(name, font=font)
    x1 = (width - text_width1) // 2
    y1 = (text_height1 // 2) - text_height1 - text_margin
    text_width2, text_height2 = draw.textsize(amount, font=font)
    x2 = (width - text_width2) // 2
    y2 = (text_height2 // 2) + text_margin
    draw.text((x1, y1), name, fill=text_color, font=font)
    draw.text((x2, y2), amount, fill=text_color, font=font)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        image.save(temp_file.name)
        print(f"Temporary file created: {temp_file.name}")
        time.sleep(5)"""
   
async def bankCommand(message):
    userID = message.author.id
    cursor.execute(f"SELECT * FROM users WHERE id = ?", (userID,))
    userCheck = cursor.fetchone()
    if userCheck:
        cursor.execute(f"SELECT bankAmt FROM users WHERE id = ?", (userID,))
        amount = (cursor.fetchone())
        money = amount[0]
        dollarCount = ["dollar","dollars"]
        if int(amount[0]) == 1:
            dollarN = dollarCount[0]
        else:
            dollarN = dollarCount[1]
        #description = f"You currently have {amount[0]} {dollarN}"
        if (money > 0) and (money <= 1000):
            bankImage = bankImgDic["0-1000"]
        elif (money > 1000) and (money <= 5000):
            bankImage = bankImgDic["1000-5000"]
        elif (money > 5000) and (money <= 10000):
            bankImage = bankImgDic["5000-10000"]
        elif (money > 10000) and (money <= 100000):
            bankImage = bankImgDic["10000-100000"]
        elif (money > 100000):
            bankImage = bankImgDic["100000+"]
        bankBuilder(message.author, money, bankImage)
        bankEmbed = await embedBuilder(None, None, discord.Color.blue(), f"attachment://combinedImage.png")
        bankEmbed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
        directory = "assets/bankImages"
        file_path = f"{directory}/combinedImage.png"
        imgFile = discord.File(file_path, filename="combinedImage.png")
        await message.channel.send(embed=bankEmbed, file=imgFile)
    else:
        await message.channel.send(f"You do not have a bank, creating now...")
        cursor.execute(f"INSERT INTO users (id, name, bankAmt, dailyTimer, job, jobTimer) VALUES (?, ?, ?, ?, ?, ?)",(userID, message.author.name, 0, 'NONE', 'NONE', 'NONE'))
        print(f"Bank created for {message.author.id}")
        connection.commit()
        await message.channel.send(f"Bank created! Have fun!")

async def cashCommand(message):
    await message.channel.send()

async def payCommand(message):
    await message.channel.send()

async def stealCommand(message):
    await message.channel.send()

async def dailyCommand(message):
    userID = message.author.id
    await sqlEcoTimer("daily", userID, message)
