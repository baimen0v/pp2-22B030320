import pygame, sys
import time
import random

from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

snake_speed = 20
speed = 10
WIDTH = 720
HEIGHT = 480
#цвет
orange = pygame.Color(255, 102, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
fruit_color = white

pygame.init()
pygame.display.set_caption('TiSoft snake')
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
#FPS
fps = pygame.time.Clock()
# начльная позиция
snake_position = [100, 50]
 

snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]


weight = random.randint(1, 3)*5
if weight==5:
    fruit_color=white
elif weight==10:
    fruit_color=orange
elif weight==15:
    fruit_color=red
fruit_position = [random.randrange(1, (WIDTH//10)) * 10,
                  random.randrange(1, (HEIGHT//10)) * 10]
disappear = pygame.USEREVENT + 1
pygame.time.set_timer(disappear, 10000)
fruit_spawn = True 

direction = 'RIGHT'
change_to = direction

level = 1
score = 0

def show_score(choice, color, font, size):
    
    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score : ' + str(score), True, color)

    score_rect = score_surface.get_rect()
    
    game_window.blit(score_surface, score_rect)

def show_level(choice, color, font, size):
    
    level_font = pygame.font.SysFont(font, size)
  
    level_surface = level_font.render('Level : ' + str(level), True, color)
 
    game_window.blit(level_surface, (0,25))

def game_over():
    pygame.display.flip()
   
    time.sleep(1)
    pygame.quit()
    quit()



while True:

    for event in pygame.event.get():
        if event.type == disappear:
            fruit_spawn = False
        if event.type == QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
   
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    if direction == 'UP':
        snake_position[1] -= speed
    if direction == 'DOWN':
        snake_position[1] += speed
    if direction == 'LEFT':
        snake_position[0] -= speed
    if direction == 'RIGHT':
        snake_position[0] += speed
 
   
    snake_body.insert(0, list((snake_position[0],snake_position[1])))

    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += weight
        fruit_spawn = False
        if score>=30*level:
            level+=1
            i = 0
          
            snake_speed+=2
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        weight = random.randint(1, 3)*5
        if weight==5:
            fruit_color=white
        elif weight==10:
            fruit_color=orange
        elif weight==15:
            fruit_color=red
        x=random.randrange(1, (WIDTH//speed)) * speed
        y=random.randrange(1, (HEIGHT//speed)) * speed
        x+=snake_position[0]%speed
        y+=snake_position[1]%speed
        fruit_position = [x,y]
        pygame.time.set_timer(disappear, 10000)
         
    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, fruit_color, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
 
    
    if snake_position[0] < 0 or snake_position[0] > WIDTH-speed:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > HEIGHT-speed:
        game_over()
     
   
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    show_score(1, white, 'times new roman', 30)
    show_level(1, white, 'times new roman', 30)
     
    
    pygame.display.update()

    fps.tick(snake_speed)