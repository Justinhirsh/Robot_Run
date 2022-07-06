import pygame

class Cannon2(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/cannon 2.png')
    RIGHT_IMAGE = pygame.image.load('resources/cannon 2.png')
    STARTING_POSITION = (575, 225)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 600
    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Cannon2.LEFT_IMAGE if direction == 'Left' else Cannon2.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), Cannon2.SIZE)
        self.rect.center = Cannon2.STARTING_POSITION
        self.direction = direction

