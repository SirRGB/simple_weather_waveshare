import logging
from PIL import Image, ImageDraw
from datetime import datetime
from timeit import default_timer as timer

from layout.display_layout_interface import DisplayInterface
from data.fetch_clock import get_date, get_clock, get_weekday
from data.fetch_weather_data import get_weather_data

logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', format='%(asctime)s %(message)s', level=logging.DEBUG)


class WeatherLayout(DisplayInterface):
    black = (0, 0, 0)
    white = (255, 255, 255)

    def get_display_output(self) -> Image:
        time = Image.new(mode='RGB', size=(self.screen_length, int(self.screen_height / 2)), color=self.white)
        d1 = ImageDraw.Draw(time)

        # draw date and clock
        date_text = f"{get_weekday()}, {get_date()}"
        d1.multiline_text(xy=(self.screen_length / 2, self.screen_height / 9), text=date_text,
                          font=self.get_font(55), fill=self.black, anchor="mm")

        clock_text = f"{get_clock()}"
        d1.multiline_text(xy=(self.screen_length / 2, self.screen_height / 2.5), text=clock_text,
                          font=self.get_font(95), fill=self.black, anchor="mm")

        self.out.paste(time, (0, 0))

        start_fetch_time = timer()
        hourly_temp, hourly_rain = get_weather_data()
        elapsed_fetch_time = timer() - start_fetch_time
        logger.info(f"Fetched data in {elapsed_fetch_time:.3f}")

        weather = Image.new(mode='RGB', size=(int(self.screen_length), int(self.screen_height / 2)),
                            color=self.white)
        d2 = ImageDraw.Draw(weather)

        legend = '\nC°\nmm'
        d2.multiline_text(xy=(int(self.screen_length / 8), int(self.screen_height / 4)), text=legend,
                          font=self.get_font(35), fill=self.black, anchor="mm")

        time_weather = ['Now']
        for i in range(1, len(hourly_temp) + 1):
            clock = datetime.now().hour + i
            if clock >= 24:
                clock = clock - 24
            time_weather.append(str(clock))

        for i in range(len(hourly_temp)):
            weather_text = f'{time_weather[i]}\n{hourly_temp[i]}\n{hourly_rain[i]}'
            d2.multiline_text(xy=(int(self.screen_length / 8 * (i + 2)), int(self.screen_height / 4)),
                              text=weather_text, font=self.get_font(35), fill=self.black, anchor="mm")

        self.out.paste(weather, (0, int(self.screen_height / 2)))

        return self.out
