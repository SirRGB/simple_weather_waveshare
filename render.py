import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

from clock import get_clock, get_date

screen_height, screen_length = 480, 800

def display():
    if sys.version_info[0] == 2:
        process = subprocess.Popen("cat /proc/cpuinfo | grep Raspberry", shell=True, stdout=subprocess.PIPE)
    else:
        process = subprocess.Popen("cat /proc/cpuinfo | grep Raspberry", shell=True, stdout=subprocess.PIPE, text=True)
    output, _ = process.communicate()
    if sys.version_info[0] == 2:
        output = output.decode(sys.stdout.encoding)

    if "Raspberry" in output:
        from lib import epd7in5_V2

        epd = epd7in5_V2.EPD()
        epd.init()
        epd.Clear()
        epd.display(create_image())
        epd.sleep()
    else:
        output = create_image()
        output.show()


def create_image():
    # create an image
    out = Image.new(mode="RGB", size=(screen_length, screen_height), color=(255, 255, 255))

    # get a font
    fnt = ImageFont.truetype(font=f"{os.path.realpath("")}/fonts/InterVariable.ttf", size=65)
    # get a drawing context
    d = ImageDraw.Draw(im=out)

    # draw date and clock
    text = f"{get_date()}\n{get_clock()}"
    d.multiline_text(xy=(screen_length / 2, screen_height / 2), text=text,
                     font=fnt, fill=(0, 0, 0), anchor="mm")

    return out