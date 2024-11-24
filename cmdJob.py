import sqlite3
import os
import discord
import random
from dotenv import load_dotenv
from datetime import datetime, timedelta
from sqlEconomy import sqlEcoTimer

load_dotenv()

database = os.getenv("DB_PATH")
connection = sqlite3.connect(database)
cursor = connection.cursor()

prefix = "$"

async def workCommand(message):
    userID = message.author.id
    cursor.execute("SELECT job FROM users WHERE id = ?", (userID,))
    userJob = cursor.fetchone()
    if userJob[0] == "NONE":
            await message.channel.send(f"You do not have a job! Use {prefix}apply to apply to your first job!")
    else:
        await sqlEcoTimer("work", userID, message)

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