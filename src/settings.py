from typing import Tuple
from pydantic import BaseModel


class Platform(BaseModel):
    image_fill: Tuple[int, int, int]


class ScreenParams:
    MAIN_WINDOW_SIZE: Tuple[int, int] = (600, 400)
    BACKGROUND_COLOR: Tuple[int, int, int] = (125, 30, 255)
    SCREEN_CAPTION: str = "The Game"

class UserSettings(BaseModel):
    FPS: int

base_platform = Platform(image_fill=(255, 255, 255))

user_settings = UserSettings(FPS=60)