import os

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont


class DisplayInterface:
    def __init__(self, screen_height:int=480, screen_length:int=800) -> None:
        self.screen_height = screen_height
        self.screen_length = screen_length
        self.font_path = f"{os.path.dirname(__file__)}/fonts/InterVariable.ttf"

        # create an image
        self.out = Image.new(mode="RGB", size=(screen_length, screen_height), color=(255, 255, 255))

        # get a drawing context
        self.d = ImageDraw.Draw(im=self.out)


    def get_font(self, size:int) -> FreeTypeFont:
        return ImageFont.truetype(font=self.font_path, size=size)


    def get_display_output(self):
        raise NotImplementedError