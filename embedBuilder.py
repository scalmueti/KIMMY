import discord
# Some Freepix photos used
async def embedBuilder(Dtitle, Ddescription, Dcolor, Dimage):
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
        embed.set_image(url=Dimage)
    return embed