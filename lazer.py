import pygame


class Lazer(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/lazer.png')
    RIGHT_IMAGE = pygame.image.load('resources/lazer.png')
    STARTING_POSITION = (300, 150)
    SIZE = (75, 25)
    SCREEN_DIM = 600, 600
    move_dist = 3



    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Lazer.LEFT_IMAGE if direction == 'Left' else Lazer.RIGHT_IMAGE
        self.rect = pygame.Rect((-100, -100), Lazer.SIZE)
        self.rect.center = Lazer.STARTING_POSITION
        self.direction = direction


    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= Lazer.move_dist
            if self.rect.right <= 0:
                self.rect.centerx = Lazer.SCREEN_DIM[0] + (Lazer.SIZE[0] / 2)
        else:
            self.rect.centerx += Lazer.move_dist
            if self.rect.left >= Lazer.SCREEN_DIM[0]:
                self.rect.centerx = - Lazer.SIZE[0] / 2

    def lvl_2(self):
        Lazer.move_dist = 5

    def reset_speed(self):
        Lazer.move_dist = 3

    def score_mode(self):
        Lazer.move_dist += 0.3