from typing import Tuple
from pydantic import BaseModel


class ColorRGB(BaseModel):
    color: Tuple[int, int, int]


class Platform(BaseModel):
    image_fill: ColorRGB


class ScreenParams(BaseModel):
    main_window_size: Tuple[int, int]
    background_color: ColorRGB
    screen_caption: str


main_screen_params = ScreenParams(
    main_window_size=(300, 300),
    background_color=ColorRGB(color=(125, 30, 255)),
    screen_caption="The game",
)

base_platform = Platform(image_fill=ColorRGB(color=(255, 255, 255)))
