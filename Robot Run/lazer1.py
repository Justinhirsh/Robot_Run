import pygame

class Lazer1(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/ultra lazer.png')
    RIGHT_IMAGE = pygame.image.load('resources/ultra lazer.png')
    STARTING_POSITION = (300, 250)
    SIZE = (379,28)
    SCREEN_DIM = 600, 600
    move_dist = 4



    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Lazer1.LEFT_IMAGE if direction == 'Left' else Lazer1.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), Lazer1.SIZE)
        self.rect.center = Lazer1.STARTING_POSITION
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Lazer1.move_dist
            if self.rect.right <= 0:
                self.rect.centerx = Lazer1.SCREEN_DIM[0] + (Lazer1.SIZE[0] / 2)
        else:
            self.rect.centerx += Lazer1.move_dist
            if self.rect.left >= Lazer1.SCREEN_DIM[0]:
                self.rect.centerx = - Lazer1.SIZE[0] / 2


