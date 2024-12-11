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

def textMaker(image, text, font_size, position=(20,20), text_color="white"):
    draw = ImageDraw.Draw(image)
    imageDirectory = "assets/fonts/LEMONMILK-Bold.otf"
    font = ImageFont.truetype(imageDirectory, font_size)
    draw.text(position, text, fill=text_color, font=font, font_size=font_size)
    return image

def circleMaker(image):
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    width, height = image.size
    circleD = min(width, height)
    draw.ellipse((0,0,circleD,circleD),fill=255)
    circImage = Image.new("RGBA", image.size)
    circImage.paste(image, (0,0), mask=mask)
    return circImage

def imageCombine(userImage, urlImage):
    images = [userImage, urlImage]
    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)
    combineImg = Image.new("RGB", (max_width, total_height), "black")
    y_offset = 0
    for img in images:
        combineImg.paste(img, (0, y_offset))
        y_offset += img.height
    directory = "assets/bankImages"
    file_path = f"{directory}/combinedImage.png"
    combineImg.save(file_path)
    os.remove("avatar_resize.png")
    os.remove("test_output.png")


def bankBuilder(user, userBank, moneyImage):
    # Placeholder
    text = f"{user.display_name}'s bank"
    img = getAvatar(user)
    size = (128,128)
    resizeImg = ImageOps.contain(img, size)
    resizeImg.save("avatar_resize.png")
    maskedImage = circleMaker(resizeImg)
    background = Image.new("RGB", (680, 180), "black")
    background.paste(maskedImage, (20, 20))
    final_image = textMaker(background, text, font_size=50, position=(170, 48), text_color="white")
    final_image.save("test_output.png")
    formatBank = "{:,}".format(userBank)
    amountImage = textMaker(final_image, str(formatBank), font_size=20, position=(170, 115), text_color="white")
    moneyResponse = requests.get(moneyImage)
    moneyResponse.raise_for_status()
    imageCombine(amountImage, Image.open(BytesIO(moneyResponse.content)))