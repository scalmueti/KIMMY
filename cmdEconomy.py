import sqlite3
import os
import discord
import random
import cmdJob
from dotenv import load_dotenv
from datetime import datetime, timedelta
from sqlEconomy import sqlEcoTimer
from embedBuilder import embedBuilder
load_dotenv()

database = os.getenv("DB_PATH")
connection = sqlite3.connect(database)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, bankAmt INTEGER, dailyTimer TEXT)")

async def bankCommand(message):
    userID = message.author.id
    cursor.execute(f"SELECT * FROM users WHERE id = ?", (userID,))
    userCheck = cursor.fetchone()
    if userCheck:
        cursor.execute(f"SELECT bankAmt FROM users WHERE id = ?", (userID,))
        amount = (cursor.fetchone())
        dollarCount = ["dollar","dollars"]
        if int(amount[0]) == 1:
            dollarN = dollarCount[0]
        else:
            dollarN = dollarCount[1]
        #bankEmbed = discord.Embed(
        #    title="Bank",
        #    description=f"You currently have {amount[0]} {dollarN}",
        #    color=discord.Color.blue()
        #)
        description = f"You currently have {amount[0]} {dollarN}"
        bankEmbed = await embedBuilder("Bank", description, discord.Color.blue(), None)
        bankEmbed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
        bankEmbed.set_footer(text="KIMMY")
        await message.channel.send(embed=bankEmbed)
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
