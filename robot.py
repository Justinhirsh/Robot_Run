import pygame


class Robot(pygame.sprite.Sprite):
    STARTING_POSITION = (300, 490)
    SIZE = (64, 64)
    IMAGE = pygame.image.load('resources/robot.png')
    MOVE_DIST = 3
    SCREEN_DIM = 600, 500
    high_score = 0
    def __init__(self):
        super().__init__()
        self.image = Robot.IMAGE
        self.rect = pygame.Rect((0, 0), Robot.SIZE)
        self.rect.center = Robot.STARTING_POSITION

        self.lives = 3

    def reset_position(self):
        self.rect.center = Robot.STARTING_POSITION
        self.lives -= 1

    def move_up(self):
        if self.rect.top >= 0:
            self.rect.centery -= Robot.MOVE_DIST

    def move_left(self):
        if self.rect.left >= 0:
            self.rect.centerx -= Robot.MOVE_DIST

    def move_down(self):
        if self.rect.bottom <= Robot.SCREEN_DIM[1] + 100:
            self.rect.centery += Robot.MOVE_DIST

    def move_right(self):
        if self.rect.right <= Robot.SCREEN_DIM[1] + 100:
            self.rect.centerx += Robot.MOVE_DIST

    def score_mode(self):
        Robot.MOVE_DIST += 0.15

    def reset_speed(self):
        Robot.move_dist = 3