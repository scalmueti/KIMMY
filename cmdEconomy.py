import sqlite3
import os
import discord
import random
import cmdJob
from dotenv import load_dotenv
from datetime import datetime, timedelta

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
        bankEmbed = discord.Embed(
            title="Bank",
            description=f"You currently have {amount[0]} {dollarN}",
            color=discord.Color.blue()
        )
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
    cursor.execute(f"SELECT dailyTimer FROM users WHERE id = ?", (userID,))
    userDailyT = cursor.fetchone()
    now = datetime.now().isoformat()
    if userDailyT[0] == "NONE":
        cursor.execute("UPDATE users SET dailyTimer = ? WHERE id = ?", (now, userID))
        dailyAmt = random.randint(50, 100)
        cursor.execute("SELECT bankAmt FROM users WHERE id = ?", (userID,))
        userBank = cursor.fetchone()
        addDaily = userBank[0] + dailyAmt
        cursor.execute("UPDATE users SET bankAmt = ? WHERE id = ?", (addDaily, userID))
        connection.commit()
        await message.channel.send(f"Daily claimed! You claimed ${dailyAmt}")
        return
    else:
        userLastClaim = datetime.fromisoformat(userDailyT[0])
        thresholdTime = userLastClaim + timedelta(hours=24)
        if (datetime.now() >= thresholdTime):
            cursor.execute("UPDATE users SET dailyTimer = ? WHERE id = ?", (now, userID))
            dailyAmt = random.randint(50, 100)
            cursor.execute("SELECT bankAmt FROM users WHERE id = ?", (userID,))
            userBank = cursor.fetchone()
            addDaily = userBank[0] + dailyAmt
            cursor.execute("UPDATE users SET bankAmt = ? WHERE id = ?", (addDaily, userID))
            connection.commit()
            await message.channel.send(f"Daily claimed! You claimed ${dailyAmt}")
        else:
            timeDiff = thresholdTime - datetime.now()
            hours = timeDiff.seconds // 3600
            minutes = (timeDiff.seconds % 3600) // 60
            seconds = timeDiff.seconds % 60
            timeFormat = f"{hours} hours, {minutes} minutes, {seconds} seconds"
            await message.channel.send(f"Unable to claim daily. Remaining time: {timeFormat}")
