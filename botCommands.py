from cmdEconomy import *

prefix = "$"
commands = ["hello", "bye"]

async def helloCommand(message):
    await message.channel.send('Hello!')
    print('Test')

async def byeCommand(message):
    await message.channel.send('Bye!')
    print('Test')

commandsDic = {
    "hello":helloCommand,
    "bye":byeCommand,
    "bank":bankCommand,
    "give":giveCommand,
    "daily":dailyCommand
}

async def commandListener(message):
    userMsg = message.content
    userMessage = userMsg.replace(f'{prefix}', "")
    if userMessage in commandsDic:
        await commandsDic[userMessage](message)
    else:
        await message.channel.send('Incorrect command.')
