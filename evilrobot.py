import pygame

class EvilRobot(pygame.sprite.Sprite):
    LEFT_IMAGE = pygame.image.load('resources/evil robot 2.png')
    RIGHT_IMAGE = pygame.image.load('resources/evil robot 1.png')
    STARTING_POSITION = (300, 250)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 600
    move_dist = 1



    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = EvilRobot.LEFT_IMAGE if direction == 'Left' else EvilRobot.RIGHT_IMAGE
        self.rect = pygame.Rect((0, 0), EvilRobot.SIZE)
        self.rect.center = EvilRobot.STARTING_POSITION
        self.direction = direction

    def move(self):
        if self.direction == 'Left':
            self.rect.centerx -= EvilRobot.move_dist
            if self.rect.right <= 0:
                self.rect.centerx = EvilRobot.SCREEN_DIM[0] + (EvilRobot.SIZE[0] / 2)
        else:
            self.rect.centerx += EvilRobot.move_dist
            if self.rect.left >= EvilRobot.SCREEN_DIM[0]:
                self.rect.centerx = - EvilRobot.SIZE[0] / 2

    def lvl_2(self):
        EvilRobot.move_dist = 3

    def reset_speed(self):
        EvilRobot.move_dist = 1

    def score_mode(self):
        EvilRobot.move_dist += 0.3
