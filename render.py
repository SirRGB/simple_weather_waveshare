import logging
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont
from timeit import default_timer as timer

from fetch_clock import get_clock, get_date, get_minute
from fetch_weather_data import get_weather_data
from parse_config import get_full_refresh

logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

screen_height, screen_length = 480, 800

def display():
    start_time = timer()

    display_output = create_image()

    if sys.version_info[0] == 2:
        process = subprocess.Popen("cat /proc/cpuinfo | grep Raspberry", shell=True, stdout=subprocess.PIPE)
    else:
        process = subprocess.Popen("cat /proc/cpuinfo | grep Raspberry", shell=True, stdout=subprocess.PIPE, text=True)
    output, _ = process.communicate()
    if sys.version_info[0] == 2:
        output = output.decode(sys.stdout.encoding)

    if "Raspberry" in output:
        logger.info("Running on Raspberry")
        from lib import epd7in5_V2

        epd = epd7in5_V2.EPD()
        if get_minute() % get_full_refresh() == 0:
            logger.info("Doing full refresh")
            epd.init()
        else:
            logger.info("Doing partial refresh")
            epd.init_fast()
        epd.Clear()
        epd.display(epd.getbuffer(display_output))
        epd.sleep()
    else:
        logger.info("Running on PC")
        display_output.show()
    elapsed_time = timer() - start_time
    logger.info(f"Completed successfully in {elapsed_time}")


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
        weather_text += f"{weather_data[0][i]}".center(8)

    weather_text += "\n"
    for i in range(len(weather_data[1])):
        weather_text += f"{weather_data[1][i]}".center(8)

    d.multiline_text(xy=(screen_length / 2, screen_height / 2 + screen_height / 4), text=weather_text,
                 font=weather_font, fill=(0, 0, 0), anchor="mm")

    return out
