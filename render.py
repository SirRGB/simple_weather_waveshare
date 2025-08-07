from PIL import Image, ImageDraw, ImageFont
from clock import get_clock, get_date
import os


screen_height, screen_length = 480, 800

def create_image():
    # create an image
    out = Image.new(mode="RGB", size=(screen_length, screen_height), color=(255, 255, 255))

    # get a font
    fnt = ImageFont.truetype(font=f"{os.path.realpath("")}/fonts/InterVariable.ttf", size=45)
    # get a drawing context
    d = ImageDraw.Draw(im=out)

    # draw date and clock
    text = f"{get_date()}\n{get_clock()}"
    d.multiline_text(xy=(screen_length/2, screen_height/2), text=text,
                     font=fnt, fill=(0, 0, 0), anchor="mm")

    out.show()