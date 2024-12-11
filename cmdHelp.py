from dictionaries import commandsList
from databaseConnect import *
from prefixPicker import prefixCheck
from embedBuilder import *
import discord

commandsInst = []

async def helpCommand(message):
    botPrefix = await prefixCheck(message)
    for x in commandsList:
        commandsInst.append(f"{botPrefix[0]}"+f"{x}\n")
    description = "".join(commandsInst)
    helpEmbed = await embedBuilder("Commands", description, discord.Color.blue(), None)
    await message.channel.send(embed=helpEmbed)