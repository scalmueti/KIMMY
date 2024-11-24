import discord
# Some Freepix photos used
async def embedBuilder(Dtitle, Ddescription, Dcolor, Dimage):
    print(Dimage)
    embed = discord.Embed(
        title = Dtitle,
        description = Ddescription,
        color = Dcolor,
    )
    if Dimage != None:
        embed.set_image(Dimage)
    return embed