import sys
import pygame
from pygame import *
import time
animation_setR = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]
animation_setL = [pygame.image.load(f"l{i}.png") for i in range(1, 6)]
pygame.init()
s=0
screen = pygame.display.set_mode((1500, 900))
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

 
class Platform(sprite.Sprite):
    def __init__(self, xx, yy):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
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
''' from random import randint
import pygame as pg
import sys
 
W = 400
H = 400
WHITE = (255, 255, 255)
 
 
class Car(pg.sprite.Sprite):# класс игрового объекта
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))
 
 
sc = pg.display.set_mode((W, H))#
 
# координата x будет случайна
car1 = Car(randint(1, W), '0.png')
 
while 1:
	#car1 = Car(randint(1, W), '0.png')
	for i in pg.event.get():
		if i.type == pg.QUIT:
			sys.exit()
 
	sc.fill(WHITE)
	sc.blit(car1.image, car1.rect)
	pg.display.update()
	pg.time.delay(20)
 
    # машинка ездит сверху вниз
	if car1.rect.y < H:
		car1.rect.y += 5
	else:
		car1 = Car(randint(1, W), '0.png')
		car1.rect.y = 0
		
 '''
