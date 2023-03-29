import pygame, sys, datetime

def rot_center(image, angle, x, y):
    rotated_img = pygame.transform.rotate(image, angle)
    new_rect = rotated_img.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_img, new_rect

pygame.init()

display = pygame.display.set_mode((800, 600))

back = pygame.image.load('images/background.jpeg')
hand_right = pygame.image.load('images/minutes.png')
hand_left = pygame.image.load('images/seconds.png')

back = pygame.transform.scale(back, (800, 600))
hand_right = pygame.transform.scale(hand_right, (300, 300))
hand_left = pygame.transform.scale(hand_left, (300, 300))

while True:

    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x = (-6*min)%360
    y = ((-1)*sec * 6)%360

    rot_right, x = rot_center(hand_right, x, 400, 300)
    rot_left, y = rot_center(hand_left, y, 400, 300)

    display.blit(back, (0, 0))
    display.blit(rot_right, x)
    display.blit(rot_left, y)

    pygame.display.update()