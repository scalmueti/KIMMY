import discord
# Some Freepix photos used
async def embedBuilder(Dtitle, Ddescription, Dcolor, Dimage):
    print(Dimage)
    if Dtitle != None:
        Dtitle = ""
    if Ddescription != None:
        Ddescription = ""
    embed = discord.Embed(
        title = Dtitle,
        description = Ddescription,
        color = Dcolor,
    )
    if Dimage != None:
        print(Dimage)
        embed.set_image(url=Dimage)
    return embed