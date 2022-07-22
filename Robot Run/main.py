import pygame,sys

from lazer1 import Lazer1
from lazer2 import Lazer2
from robot import Robot
from evilrobot import EvilRobot
from lazer import Lazer
from boss import Boss
from cannon1 import Cannon1
from cannon2 import Cannon2
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (21, 237, 32)
YELLOW = (237, 233, 21)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 255)
pygame.init()
ICON = pygame.image.load("resources/menu_image.png")
score_mode = False
pygame.display.set_icon(ICON)
# music_file = pygame.mixer.Sound("resources/backround music.mp3")
# music_file.play()

def play(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

background_music = "resources/background music.ogg"
win_music = "resources/congradulations.ogg"
boss_music = "resources/boss music.ogg"
play(background_music)
pygame.mixer.music.set_volume(0.3)
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
SCREEN_DIM = WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('Robot Run!')
CLOCK = pygame.time.Clock()
FPS = 60
FONT = pygame.font.Font('resources/font.ttf', 20)
MENU_BIG = pygame.font.Font('resources/font.ttf', 60)
MENU_MED = pygame.font.Font('resources/font.ttf', 25)
MENU_SMALL = pygame.font.Font('resources/font.ttf', 15)
MENU_IMAGE = pygame.image.load('resources/menu_image.png')
END_IMAGE = pygame.image.load('resources/dead robot.png')
level = 0
START_MENU = True
END_MENU = False
boss_mode = False
robot = Robot()
evilrobot = EvilRobot(EvilRobot.STARTING_POSITION, 'Left')
lazer = Lazer(Lazer.STARTING_POSITION, 'Right')
lazer2 = Lazer2(Lazer2.STARTING_POSITION, 'Right')
lazer1 = Lazer1(Lazer1.STARTING_POSITION, 'Left')
boss = Boss(Boss.STARTING_POSITION, 'Left')
cannon1 = Cannon1(Cannon1.STARTING_POSITION, 'Left')
cannon2 = Cannon2(Cannon1.STARTING_POSITION, 'Right')
score = 0
current_best = 0
high_score = 0
score_file = open("score.txt", "r+")
win_music_play = 1
try:
    high_score = int(score_file.readline().strip())
except:
    print("No high score, reseting")
    score_file.truncate(0)
    score_file.seek(0)
    score_file.write(str(0))
best_score = high_score
#background code
window = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND = pygame.image.load('background.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH,HEIGHT))
boss_music_play = 1
BACKGROUND_MENU = pygame.image.load('background menu.jpg')
BACKGROUND_MENU = pygame.transform.scale(BACKGROUND_MENU,(WIDTH,HEIGHT))
LEVEL_1 = pygame.image.load('resources/level 1.png')
LEVEL_1 = pygame.transform.scale(LEVEL_1,(WIDTH,HEIGHT))
LEVEL_2 = pygame.image.load('resources/level 2.png')
LEVEL_2 = pygame.transform.scale(LEVEL_2,(WIDTH,HEIGHT))
LEVEL_3 = pygame.image.load('resources/level 3.png')
LEVEL_3 = pygame.transform.scale(LEVEL_3,(WIDTH,HEIGHT))
YOU_WIN = pygame.image.load('resources/you win.png')
YOU_WIN = pygame.transform.scale(YOU_WIN,(WIDTH,HEIGHT))
while(True):
    # pygame.mixer.music.load("resources/background music.ogg")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.3)


    while START_MENU:
        CLOCK.tick(15)
        window.blit(BACKGROUND_MENU,(0,0))
        name = MENU_BIG.render('ROBOT RUN', True, WHITE)
        instructions = MENU_SMALL.render('Press Space To Start', True, WHITE)
        SCREEN.blit(name, (75, 130))
        SCREEN.blit(instructions, (180, 210))
        SCREEN.blit(MENU_IMAGE, (145, 260))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    window.blit(LEVEL_1, (0, 0))
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    START_MENU = False

    while END_MENU:
        CLOCK.tick(15)
        window.blit(BACKGROUND_MENU,(0,0))
        thx = MENU_MED.render('You Died', True, RED)
        scores = MENU_MED.render('Your Final Score: %d' % (score), True, WHITE)
        instructions = MENU_SMALL.render('Press \'Space\' To Play Again', True, WHITE)
        SCREEN.blit(thx, (85, 120))
        SCREEN.blit(scores, (70, 180))
        SCREEN.blit(END_IMAGE, (145, 260))
        SCREEN.blit(instructions, (130, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if high_score > best_score:
                    score_file.seek(0)
                    score_file.truncate(0)
                    score_file.write(str(high_score))
                score_file.close()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play(background_music)
                    END_MENU = False
                    score_mode = False
                    current_best = 0
                    score = 0
                    robot.lives = 3
                    lazer.reset_speed()
                    evilrobot.reset_speed()
                    robot.reset_speed()
                    level = 0
                    boss_mode = False
                    boss_music_play = 1
                    win_music_play = 1
        pygame.display.update()



    while level == 9:
        CLOCK.tick(15)
        window.blit(YOU_WIN, (0, 0))
        pygame.display.update()
        if win_music_play == 1:
            play(win_music)
            win_music_play = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if high_score > best_score:
                    score_file.seek(0)
                    score_file.truncate(0)
                    score_file.write(str(high_score))
                score_file.close()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score_mode = True
                    play(background_music)
                    level += 1

        pygame.display.update()
    if robot.lives == 0:
        END_MENU = True
        robot.reset_speed()



    CLOCK.tick(FPS)
    window.blit(BACKGROUND,(0,0))
    SCREEN.blit(robot.image, robot.rect)
    if level <= 5 or level >= 10:
        SCREEN.blit(lazer.image, lazer.rect)
        SCREEN.blit(evilrobot.image, evilrobot.rect)
        if robot.rect.colliderect(evilrobot.rect):
            robot.reset_position()
        if robot.rect.colliderect(lazer.rect):
            robot.reset_position()




    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_w]:
        robot.move_up()
    if keypress[pygame.K_s]:
        robot.move_down()
    if keypress[pygame.K_a]:
        robot.move_left()
    if keypress[pygame.K_d]:
        robot.move_right()


    score_text = FONT.render("Score: " + str(score + current_best), True, WHITE)
    high_score_text = FONT.render("High Score: " + str(high_score), True, WHITE)
    lives_text = FONT.render("Lives: " + str(robot.lives), True, WHITE)
    level_text = FONT.render("Level: " + str(level - 9), True, WHITE)
    SCREEN.blit(score_text, (5, 0))
    SCREEN.blit(high_score_text, (5, 20))
    SCREEN.blit(lives_text, (5, 40))
    if boss_mode == True:

         SCREEN.blit(boss.image, boss.rect)
         SCREEN.blit(lazer1.image, lazer1.rect)
         SCREEN.blit(lazer2.image, lazer2.rect)
         SCREEN.blit(cannon1.image, cannon1.rect)
         SCREEN.blit(cannon2.image, cannon2.rect)
         if robot.rect.colliderect(lazer1.rect):
             robot.reset_position()
         if robot.rect.colliderect(lazer2.rect):
             robot.reset_position()

         pygame.display.update()
    if score_mode == True:
        SCREEN.blit(level_text, (5, 60))



    if 475 - robot.rect.top > current_best:
        current_best = 475 - robot.rect.top

    if score + current_best >= high_score:
        high_score = score + current_best
    if robot.rect.top <= 20:
        robot.reset_position()
        level += 1
        if level >= 9:
            boss_mode = False
            evilrobot.score_mode()
            lazer.score_mode()
            robot.score_mode()

        if level == 3:
            window.blit(LEVEL_2, (0, 0))
            pygame.display.flip()
            pygame.time.wait(2000)
            evilrobot.lvl_2()
            lazer.lvl_2()
        if level == 6:
            if boss_music_play == 1:
                play(boss_music)
                boss_music_play = 2
            window.blit(LEVEL_3, (0, 0))
            pygame.display.flip()
            pygame.time.wait(2000)
            boss_mode = True
        robot.lives += 1
        score += 1000 + current_best
        current_best = 0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            if high_score > best_score:
                score_file.seek(0)
                score_file.truncate(0)
                score_file.write(str(high_score))
            score_file.close()
            sys.exit()
            pygame.mixer.music.unload()
            sys.exit()



    evilrobot.move()
    lazer.move()
    lazer1.move()
    lazer2.move()
    pygame.display.flip()

