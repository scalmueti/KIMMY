from discord import Embed
# Some Freepix photos used
async def embedBuilder(title, Ddesc, color, image):
    embed = Embed(title=title, description=Ddesc, color=color)
    if image:
        embed.set_image(image=image)
    return embed