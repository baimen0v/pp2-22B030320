import pygame
import sys
import random
import time
from pygame.locals import *


pygame.init()


FPS = 60
FramePerSec = pygame.time.Clock()


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACK_OVER = (122, 222, 172)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0


sound1 = pygame.mixer.Sound('background.wav')
sound2 = pygame.mixer.Sound('crash.wav')


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, WHITE)


SPEED_FLAG = 1


background = pygame.image.load("road.png")


DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rand = random.randint(1, 3)
        self.weight = self.rand*5
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (self.rand*15, self.rand*15))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, 10)
        if (self.rect.top > 600):
            
            self.reinit()

    def reinit(self):
        self.rand = random.randint(1, 3)
        self.weight = self.rand*5
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (self.rand*15, self.rand*15))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

# enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# main objects
P1 = Player()
E1 = Enemy()
coin = Coin()

# groups of objects
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin)
coin_group = pygame.sprite.Group()
coin_group.add(coin)


INC_SPEED = pygame.USEREVENT + 1


while True:
   
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("passsed: "+str(SCORE), True, BLACK)
    coin_scores = font_small.render('coins: ' + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (300, 10))

    # moving
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

   
    if pygame.sprite.spritecollideany(P1, coin_group):
        for entity in coin_group:
            COIN_SCORE += entity.weight
            entity.reinit()
            if COIN_SCORE >= (60*SPEED_FLAG):
                SPEED_FLAG += 1
                SPEED += 2.5
            entity.rect.top = 0
            entity.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

   
    if pygame.sprite.spritecollideany(P1, enemies):
        
        time.sleep(0.5)

        DISPLAYSURF.fill(BACK_OVER)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)