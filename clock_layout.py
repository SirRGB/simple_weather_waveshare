from PIL.Image import Image

from display_layout_interface import DisplayInterface
from fetch_clock import get_clock, get_date, get_weekday


class ClockLayout(DisplayInterface):
    def get_display_output(self) -> Image:
        text = f"{get_weekday()}\n{get_date()}\n{get_clock()}"
        self.d.multiline_text(xy=(self.screen_length / 2, self.screen_height / 2), text=text,
            font=self.get_font(95), fill=(0, 0, 0), anchor="mm")
        return self.out
