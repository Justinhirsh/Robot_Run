import pygame

class Cannon1(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/cannon.png')
    RIGHT_IMAGE = pygame.image.load('resources/cannon.png')
    STARTING_POSITION = (-40, 125)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 600
    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Cannon1.LEFT_IMAGE if direction == 'Left' else Cannon1.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), Cannon1.SIZE)
        self.rect.center = Cannon1.STARTING_POSITION
        self.direction = direction

