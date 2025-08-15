import logging
from PIL.Image import Image
from timeit import default_timer as timer

from layout.display_layout_interface import DisplayInterface
from data.fetch_clock import get_date, get_clock, get_weekday
from data.fetch_weather_data import get_weather_data

logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

class WeatherLayout(DisplayInterface):
    def get_display_output(self) -> Image:
        # draw date and clock
        date_text = f"{get_weekday()}, {get_date()}"
        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 4), text=date_text,
                              font=self.get_font(55), fill=(0, 0, 0), anchor="mm")


        clock_text = f"{get_clock()}"
        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 2), text=clock_text,
                              font=self.get_font(95), fill=(0, 0, 0), anchor="mm")


        start_fetch_time = timer()
        weather_data = get_weather_data()
        elapsed_fetch_time = timer() - start_fetch_time
        logger.info(f"Rendered in {elapsed_fetch_time:.3f}")

        weather_text = ""
        for i in range(len(weather_data[0])):
            weather_text += f"{weather_data[0][i]:^8}"

        weather_text += "\n"
        for i in range(len(weather_data[1])):
            weather_text += f"{weather_data[1][i]:^8}"

        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 2 + self.screen_height / 4),
                              text=weather_text, font=self.get_font(35), fill=(0, 0, 0), anchor="mm")

        return self.out
