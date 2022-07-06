import pygame


class Lazer2(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/ultra lazer2.png')
    RIGHT_IMAGE = pygame.image.load('resources/ultra lazer2.png')
    STARTING_POSITION = (300, 150)
    SIZE = (379,28)
    SCREEN_DIM = 600, 600
    move_dist = 4



    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Lazer2.LEFT_IMAGE if direction == 'Left' else Lazer2.RIGHT_IMAGE
        self.rect = pygame.Rect((-100, -100), Lazer2.SIZE)
        self.rect.center = Lazer2.STARTING_POSITION
        self.direction = direction


    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Lazer2.move_dist
            if self.rect.right <= 0:
                self.rect.centerx = Lazer2.SCREEN_DIM[0] + (Lazer2.SIZE[0] / 2)
        else:
            self.rect.centerx += Lazer2.move_dist
            if self.rect.left >= Lazer2.SCREEN_DIM[0]:
                self.rect.centerx = - Lazer2.SIZE[0] / 2

