import sqlite3
import os
from dotenv import load_dotenv

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
        await message.channel.send(f"This is {message.author}'s bank: {amount[0]}")
    else:
        await message.channel.send(f"You do not have a bank, creating now...")
        cursor.execute(f"INSERT INTO users (id, name, bankAmt, dailyTimer) VALUES (?, ?, ?, ?)",(userID, message.author.name, 0, 'NONE'))
        print(f"Bank created for {message.author.id}")
        connection.commit()
        await message.channel.send(f"Bank created! Have fun!")

async def giveCommand(message):
    await message.channel.send()

async def dailyCommand(message):
    await message.channel.send()