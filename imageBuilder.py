import os
from io import BytesIO
import discord
import requests
from PIL import Image, ImageDraw, ImageOps, ImageFont

def getAvatar(user):
    avatarURL = user.avatar
    response = requests.get(avatarURL)
    img = Image.open(BytesIO(response.content))
    return img

def textMaker(image, text, font_size=20, position=(10,10), text_color="white"):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text(position, text, fill=text_color, font=font)
    return image

def bankBuilder(user, userBank):
    # Placeholder
    text = user.global_name
    img = getAvatar(user)
    size = (128,128)
    resizeImg = ImageOps.contain(img, size)
    resizeImg.save("avatar_resize.png")
    background = Image.new("RGB", (680, 240), "black")
    background.paste(resizeImg, (20, 20))
    final_image = textMaker(background, text, font_size=20, position=(20, background.height))
    final_image.save("test_output.png")
    print(userBank)