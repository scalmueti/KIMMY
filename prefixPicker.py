import os
import sqlite3
from databaseConnect import *

database = os.getenv("DB_PATH")
dbPath = os.path.join(database, "guildDB.db")
connection = sqlite3.connect(dbPath)
cursor = connection.cursor()

async def prefixCheck(message):
    #cursor, connection = await dbPick("guild")
    cursor.execute("CREATE TABLE IF NOT EXISTS guilds (guildid INTEGER PRIMARY KEY, name TEXT, prefix TEXT)")
    guildID = message.guild.id
    guildName = message.guild.name
    cursor.execute("SELECT * FROM guilds WHERE guildid = ?", (guildID,))
    prefixCheck = cursor.fetchone()
    if prefixCheck:
        cursor.execute("SELECT prefix FROM guilds WHERE guildid = ?", (guildID,))
        currPrefix = cursor.fetchone()
        connection.commit()
        return currPrefix
    else:
        cursor.execute("INSERT INTO guilds (guildid, name, prefix) VALUES (?, ?, ?)", (guildID, guildName, "$"))
        connection.commit()
    
async def prefixCommand(message, newPrefix):
    guildID = message.guild.id
    cursor.execute("UPDATE guilds SET prefix = ? WHERE guildid = ?", (newPrefix, guildID))
    connection.commit()
    await message.channel.send(f"Prefix has been changed to `{newPrefix}`")
