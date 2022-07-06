import pygame

class Boss(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/thedestroyer.png')
    RIGHT_IMAGE = pygame.image.load('resources/thedestroyer.png')
    STARTING_POSITION = (215,0)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 600
    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Boss.LEFT_IMAGE if direction == 'Left' else Boss.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), Boss.SIZE)
        self.rect.center = Boss.STARTING_POSITION
        self.direction = direction

