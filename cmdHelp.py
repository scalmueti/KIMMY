from dictionaries import commandsList,botPrefix
from embedBuilder import *

commandsInst = []

async def helpCommand(message):
    for x in commandsList:
        commandsInst.append(f"{botPrefix}"+f"{x}\n")
    description = "".join(commandsInst)
    print(description)
    helpEmbed = await embedBuilder("Commands", description, discord.Color.blue(), None)
    await message.channel.send(embed=helpEmbed)