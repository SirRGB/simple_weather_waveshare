import os

from PIL import Image, ImageDraw, ImageFont

from fetch_clock import get_clock, get_date
from fetch_weather_data import get_weather_data


class Display:
    def __init__(self, screen_height:int=480, screen_length:int=800):
        self.screen_height = screen_height
        self.screen_length = screen_length
        self.font_path = f"{os.path.dirname(__file__)}/fonts/InterVariable.ttf"

        # create an image
        self.out = Image.new(mode="RGB", size=(screen_length, screen_height), color=(255, 255, 255))

        # get a drawing context
        self.d = ImageDraw.Draw(im=self.out)


    def set_font(self, size:int):
        # get a font
        return ImageFont.truetype(font=self.font_path, size=size)


    def get_weather_display(self):
        # draw date and clock
        date_text = f"{get_date()}"
        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 4), text=date_text,
                         font=self.set_font(55), fill=(0, 0, 0), anchor="mm")


        clock_font = ImageFont.truetype(font=self.font_path, size=95)
        clock_text = f"{get_clock()}"
        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 2), text=clock_text,
                         font=clock_font, fill=(0, 0, 0), anchor="mm")


        weather_font = ImageFont.truetype(font=self.font_path, size=35)
        weather_data = get_weather_data()
        weather_text = ""
        for i in range(len(weather_data[0])):
            weather_text += f"{weather_data[0][i]:^8}"

        weather_text += "\n"
        for i in range(len(weather_data[1])):
            weather_text += f"{weather_data[1][i]:^8}"

        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 2 + self.screen_height / 4), text=weather_text,
                         font=weather_font, fill=(0, 0, 0), anchor="mm")

        return self.out
