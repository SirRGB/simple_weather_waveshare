from PIL import Image, ImageDraw, ImageFont
from clock import get_clock, get_date

def create_image():
    # create an image
    out = Image.new("RGB", (800, 480), (255, 255, 255))

    # get a font
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw date and clock
    d.multiline_text((10, 10), get_date(), font=fnt, fill=(0, 0, 0))
    d.multiline_text((10, 50), get_clock(), font=fnt, fill=(0, 0, 0))

    out.show()