import sqlite3
import os
import random
from dictionaries import jobsDic
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

database = os.getenv("DB_PATH")
connection = sqlite3.connect(database)
cursor = connection.cursor()

async def sqlEcoTimer(type, userID, message):
    if type == "daily":
        cursor.execute("SELECT dailyTimer FROM users WHERE id = ?", (userID,))
        ecoTimer = cursor.fetchone()
        timerType = "dailyTimer"
        userPay = random.randint(250,500)
    elif type == "work":
        cursor.execute("SELECT jobTimer FROM users WHERE id = ?", (userID,))
        ecoTimer = cursor.fetchone()
        timerType = "jobTimer"
        cursor.execute("SELECT job FROM users WHERE id = ?", (userID,))
        userJob = cursor.fetchone()
        jobInfo = jobsDic[userJob[0]]
        userPay = jobInfo[0]
    else:
          pass
    if ecoTimer[0] == "NONE":
            now = datetime.now().isoformat()
            cursor.execute(f"UPDATE users SET {timerType} = ? WHERE id = ?", (now, userID))
            payAmt = userPay
            cursor.execute("SELECT bankAmt FROM users WHERE id = ?", (userID,))
            userBank = cursor.fetchone()
            addJob = userBank[0] + payAmt
            cursor.execute("UPDATE users SET bankAmt = ? WHERE id = ?", (addJob, userID))
            connection.commit()
            if type == "work":
                 await message.channel.send(f"You went to work! You claimed ${payAmt}")
            elif type == "daily":
                 await message.channel.send(f"Daily claimed! You claimed ${payAmt}")
            else:
                 pass
    else:
            userLastClaim = datetime.fromisoformat(ecoTimer[0])
            thresholdTime = userLastClaim + timedelta(hours=24)
            if (datetime.now() >= thresholdTime):
                cursor.execute(f"UPDATE users SET {timerType} = ? WHERE id = ?", (now, userID))
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
                if type == "work":
                     await message.channel.send(f"Unable to work. Remaining time: {timeFormat}")
                elif type == "daily":
                     await message.channel.send(f"Unable to claim daily. Remaining time: {timeFormat}")