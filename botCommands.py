from cmdEconomy import *
from cmdJob import *

prefix = "$"

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
    "pay":payCommand,
    "daily":dailyCommand,
    "work":workCommand,
    "cash":cashCommand,
    "job":jobCommand,
    "steal":stealCommand,
    "apply":applyCommand
}

async def commandListener(message):
    userMsg = message.content
    userMessage = userMsg.replace(f'{prefix}', "")
    if userMessage in commandsDic:
        await commandsDic[userMessage](message)
    else:
        await message.channel.send('Incorrect command.')
