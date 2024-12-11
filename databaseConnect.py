import os
import sqlite3

async def dbPick(type):
    database = os.getenv("DB_PATH")
    if type == "user":
        dbPath = os.path.join(database, "userDB.db")
    elif type == "guild":
        dbPath = os.path.join(database, "guildDB.db")
    else:
        pass
    connection = sqlite3.connect(dbPath)
    cursor = connection.cursor()
    dbInfo = [cursor, connection]
    return dbInfo[0], dbInfo[1]