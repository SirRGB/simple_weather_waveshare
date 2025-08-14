import os

from PIL import Image, ImageDraw, ImageFont

from fetch_clock import get_clock, get_date
from fetch_weather_data import get_weather_data

screen_height, screen_length = 480, 800

def create_image():
    font_path = f"{os.path.dirname(__file__)}/fonts/InterVariable.ttf"

    # create an image
    out = Image.new(mode="RGB", size=(screen_length, screen_height), color=(255, 255, 255))

    # get a font
    date_font = ImageFont.truetype(font=font_path, size=55)
    # get a drawing context
    d = ImageDraw.Draw(im=out)

    # draw date and clock
    date_text = f"{get_date()}"
    d.multiline_text(xy=(screen_length / 2, screen_height / 4), text=date_text,
                     font=date_font, fill=(0, 0, 0), anchor="mm")


    clock_font = ImageFont.truetype(font=font_path, size=95)
    clock_text = f"{get_clock()}"
    d.multiline_text(xy=(screen_length / 2, screen_height / 2), text=clock_text,
                     font=clock_font, fill=(0, 0, 0), anchor="mm")


    weather_font = ImageFont.truetype(font=font_path, size=35)
    weather_data = get_weather_data()
    weather_text = ""
    for i in range(len(weather_data[0])):
        weather_text += f"{weather_data[0][i]:^8}"

    weather_text += "\n"
    for i in range(len(weather_data[1])):
        weather_text += f"{weather_data[1][i]:^8}"

    d.multiline_text(xy=(screen_length / 2, screen_height / 2 + screen_height / 4), text=weather_text,
                     font=weather_font, fill=(0, 0, 0), anchor="mm")

    return out
