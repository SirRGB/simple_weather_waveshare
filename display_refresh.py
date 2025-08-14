import logging
import subprocess
import sys
from timeit import default_timer as timer

from clock_layout import ClockLayout
from fetch_clock import get_minute
from parse_config import get_full_refresh, get_display_target
from weather_layout import WeatherLayout

logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

def refresh():
    start_time = timer()

    if get_display_target() == "weather":
        display_output = WeatherLayout().get_display_output()
    else:
        display_output = ClockLayout().get_display_output()

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
            logger.info("Doing fast refresh")
            epd.init_fast()
        epd.Clear()
        epd.display(epd.getbuffer(display_output))
        epd.sleep()
    else:
        logger.info("Running on PC")
        display_output.show()
    elapsed_time = timer() - start_time
    logger.info(f"Completed successfully in {elapsed_time}")