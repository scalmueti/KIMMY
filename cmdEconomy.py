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
from databaseConnect import *
import tempfile
import time
load_dotenv()

async def bankCommand(message):
    cursor, connection = await dbPick("user")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, bankAmt INTEGER, dailyTimer TEXT)")
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
        connection.commit()
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
