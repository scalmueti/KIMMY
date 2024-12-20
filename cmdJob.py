import sqlite3
import os
import discord
import random
from dotenv import load_dotenv
from datetime import datetime, timedelta
from databaseConnect import *
from sqlEconomy import sqlEcoTimer
from dictionaries import jobsDic

load_dotenv()

prefix = "$"

async def workCommand(message):
    cursor, connection = await dbPick("user")
    userID = message.author.id
    cursor.execute("SELECT job FROM users WHERE id = ?", (userID,))
    userJob = cursor.fetchone()
    if userJob[0] == "NONE":
        await message.channel.send(f"You do not have a job! Use {prefix}apply to apply to your first job!")
        connection.commit()
    else:
        await sqlEcoTimer("work", userID, message)

async def jobCommand(message):
    cursor, connection = await dbPick("user")
    userID = message.author.id
    cursor.execute("SELECT job FROM users WHERE id = ?", (userID,))
    userJob = cursor.fetchone()
    connection.commit()
    await message.channel.send(f"You work as a {jobsDic[userJob[0]][1]}")

async def applyCommand(message):
    cursor, connection = await dbPick("user")
    userID = message.author.id
    cursor.execute("SELECT job FROM users WHERE id = ?", (userID,))
    userJob = cursor.fetchone()
    if userJob[0] == 'NONE':
        await message.channel.send(f"You're unemployed! Applying you to be a fast food worker...")
        cursor.execute("UPDATE users SET job = ? WHERE id = ?", ("FFWorker", userID))
        connection.commit()
    else:
        pass