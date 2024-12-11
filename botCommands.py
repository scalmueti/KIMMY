from cmdEconomy import *
from cmdJob import *
from cmdHelp import *
from prefixPicker import prefixCommand

prefix = "$"

async def helloCommand(message):
    await message.channel.send('Hello!')

async def byeCommand(message):
    await message.channel.send('Bye!')

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
    "apply":applyCommand,
    "help":helpCommand,
    "prefix":prefixCommand
}

async def commandListener(message):
    userMsg = message.content
    msgParts = userMsg[len(prefix):].split()
    cmdName = msgParts[0]
    args = msgParts[1:] if len (msgParts) > 1 else []
    if args and cmdName in commandsDic:
        await commandsDic[cmdName](message, *args)
    elif cmdName in commandsDic:
        await commandsDic[cmdName](message)
    else:
        await message.channel.send('Incorrect command.')
