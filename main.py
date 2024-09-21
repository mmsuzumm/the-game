import pygame

from src.settings import main_screen_params as msp

pygame.init()

screen = pygame.display.set_mode(msp.main_window_size)
screen.fill(msp.background_color.color)

pygame.display.set_caption(msp.screen_caption)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
