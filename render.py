from PIL import Image, ImageDraw, ImageFont
from clock import get_clock, get_date

screen_height, screen_length = 480, 800

def create_image():
    # create an image
    out = Image.new("RGB", (screen_length, screen_height), (255, 255, 255))

    # get a font
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw date and clock
    text = f"{get_date()}\n{get_clock()}"
    d.multiline_text((screen_length/2, screen_height/2), text,
                     font=fnt, fill=(0, 0, 0), anchor="mm")

    out.show()