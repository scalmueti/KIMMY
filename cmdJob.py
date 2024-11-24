import sqlite3
import os
import discord
import random
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

database = os.getenv("DB_PATH")
connection = sqlite3.connect(database)
cursor = connection.cursor()

lowPay = random.randint(500,1000)
lowmedPay = random.randint(1000,2500)
medPay = random.randint(2500,5000)
medhPay = random.randint(5000,7500)
highPay = random.randint(10000,15000)
ultraPay = random.randint(25000,50000)

jobsDic = {
        "FFWorker":[lowPay, "Fast Food Worker"],
        "Barista":[lowPay, "Barista"],
        "Waiter":[lowPay, "Waiter"],
        "SecGuard":[lowmedPay, "Security Guard"],
        "Teacher":[lowmedPay, "Teacher"],
        "Plumber":[medPay, "Plumber"],
        "SalesA":[medhPay, "Sales Associate"],
        "NurseA":[medhPay, "Nurse Associate"],
        "IT Manger":[highPay, "IT Manager"],
        "SoftDev":[highPay, "Software Developer"],
        "Surgeon":[ultraPay, "Surgeon"],
        "Lawyer":[ultraPay, "Lawyer"]
}

async def workCommand(message):
    userID = message.author.id
    cursor.execute("SELECT job FROM users WHERE id = ?", (userID,))
    userJob = cursor.fetchone()
    jobInfo = jobsDic[userJob[0]]
    userPay = jobInfo[0]
    cursor.execute(f"SELECT jobTimer FROM users WHERE id = ?", (userID,))
    userJobT = cursor.fetchone()
    now = datetime.now().isoformat()
    if userJobT[0] == "NONE":
        cursor.execute("UPDATE users SET jobTimer = ? WHERE id = ?", (now, userID))
        jobAmt = userPay
        cursor.execute("SELECT bankAmt FROM users WHERE id = ?", (userID,))
        userBank = cursor.fetchone()
        addJob = userBank[0] + jobAmt
        cursor.execute("UPDATE users SET bankAmt = ? WHERE id = ?", (addJob, userID))
        connection.commit()
        await message.channel.send(f"You went to work! You claimed ${jobAmt}")
        return
    else:
        userLastClaim = datetime.fromisoformat(userJobT[0])
        thresholdTime = userLastClaim + timedelta(hours=24)
        if (datetime.now() >= thresholdTime):
            cursor.execute("UPDATE users SET jobTimer = ? WHERE id = ?", (now, userID))
            jobAmt = userPay
            cursor.execute("SELECT bankAmt FROM users WHERE id = ?", (userID,))
            userBank = cursor.fetchone()
            addJob = userBank[0] + jobAmt
            cursor.execute("UPDATE users SET bankAmt = ? WHERE id = ?", (addJob, userID))
            connection.commit()
            await message.channel.send(f"You went to work! You claimed ${jobAmt}")
        else:
            timeDiff = thresholdTime - datetime.now()
            hours = timeDiff.seconds // 3600
            minutes = (timeDiff.seconds % 3600) // 60
            seconds = timeDiff.seconds % 60
            timeFormat = f"{hours} hours, {minutes} minutes, {seconds} seconds"
            await message.channel.send(f"Unable to work. Remaining time: {timeFormat}")

async def jobCommand(message):
    userID = message.author.id
    cursor.execute("SELECT job FROM users WHERE id = ?", (userID,))
    userJob = cursor.fetchone()
    connection.commit()
    await message.channel.send()

async def applyCommand(message):
    userID = message.author.id
    cursor.execute("SELECT job FROM users WHERE id = ?", (userID,))
    userJob = cursor.fetchone()
    if userJob[0] == 'NONE':
        await message.channel.send(f"You're unemployed! Applying you to be a fast food worker...")
        cursor.execute("UPDATE users SET job = ? WHERE id = ?", ("FFWorker", userID))
        connection.commit()
    else:
        pass