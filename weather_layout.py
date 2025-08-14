from PIL.Image import Image

from display_layout_interface import DisplayInterface
from fetch_clock import get_date, get_clock, get_weekday
from fetch_weather_data import get_weather_data


class WeatherLayout(DisplayInterface):
    def get_display_output(self) -> Image:
        # draw date and clock
        date_text = f"{get_weekday()}, {get_date()}"
        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 4), text=date_text,
                              font=self.get_font(55), fill=(0, 0, 0), anchor="mm")


        clock_text = f"{get_clock()}"
        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 2), text=clock_text,
                              font=self.get_font(95), fill=(0, 0, 0), anchor="mm")


        weather_data = get_weather_data()
        weather_text = ""
        for i in range(len(weather_data[0])):
            weather_text += f"{weather_data[0][i]:^8}"

        weather_text += "\n"
        for i in range(len(weather_data[1])):
            weather_text += f"{weather_data[1][i]:^8}"

        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 2 + self.screen_height / 4), text=weather_text,
                              font=self.get_font(35), fill=(0, 0, 0), anchor="mm")

        return self.out
