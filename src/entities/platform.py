import pygame


from settings import base_platform


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(base_platform.image_fill)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
