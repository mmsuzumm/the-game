import sys
from os.path import dirname, join

sys.path.append(join(dirname(__file__), "src"))

import pygame

from settings import ScreenParams, user_settings
from entities.levels.first import load_level


pygame.init()

screen = pygame.display.set_mode(ScreenParams.MAIN_WINDOW_SIZE)
clock = pygame.time.Clock()

pygame.display.set_caption(ScreenParams.SCREEN_CAPTION)
pygame.display.flip()


platforms = load_level()
platform_sprites = pygame.sprite.Group()
platform_sprites.add(platforms)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(ScreenParams.BACKGROUND_COLOR)
    platform_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(user_settings.FPS)
