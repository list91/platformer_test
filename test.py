

import sys
import pygame
from pygame import *
import time
animation_setR = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]
animation_setL = [pygame.image.load(f"l{i}.png") for i in range(1, 6)]
pygame.init()
s=0
screen = pygame.display.set_mode((1000, 1000))
rect = pygame.Rect(0, 0, 0, 0)
s = pygame.image.load("0.png")
x=311
y=247#447
animation_set = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]
window = screen
clock = pygame.time.Clock()
i = 0
#blocks
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

 
class Platform():
    def __init__(self, x, y):
       
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
#
level = [
       "----------------------------------",
       "-                                -",
       "-                       --       -",
       "-                                -",
       "-            --                  -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                   ----     --- -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                            --- -",
       "-                                -",
       "-                                -",
       "-      ---                       -",
       "-                                -",
       "-   -------         ----         -",
       "-                                -",
       "-                         -      -",
       "-                            --  -",
       "-                                -",
       "-                                -",
       "----------------------------------"]
platforms = []
xx=yy=0 # координаты
for row in level: # вся строка
        for col in row: # каждый символ
            if col == "-":
                pf = Platform(xx,yy)
                pygame.sprite.Group.add(pf)
                platforms.append(pf)

            xx += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
        yy += PLATFORM_HEIGHT    #то же самое и с высотой
        xx = 0                   #на каждой новой строчке начинаем с нуля
#

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(s, (x, y))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        window.fill((0,0,0))
        window.blit(animation_setR[i // 12], (x, y))
        i += 1
        x+=1
        if i == 60:
            i = 0
    elif keys[pygame.K_LEFT]:
        window.fill((0,0,0))
        window.blit(animation_setL[i // 12], (x, y))
        i += 1
        x-=1
        if i == 60:
            i = 0
    pygame.display.flip()
    window.fill((0, 0, 0))
    clock.tick(100)
    print(x)
    
