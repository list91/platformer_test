from random import randint
from pygame import *
import pygame
import sys
import os
import pyganim
W = 400
H = 400
WHITE = (255, 255, 255)
 
 
 

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
JUMP_POWER = 10
GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1 # скорость смены кадров
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/r1.png' % ICON_DIR),
            ('%s/r2.png' % ICON_DIR),
            ('%s/r3.png' % ICON_DIR),
            ('%s/r4.png' % ICON_DIR),
            ('%s/r5.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/l1.png' % ICON_DIR),
            ('%s/l2.png' % ICON_DIR),
            ('%s/l3.png' % ICON_DIR),
            ('%s/l4.png' % ICON_DIR),
            ('%s/l5.png' % ICON_DIR)]

class man(sprite.Sprite):# класс игрового объекта
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
  #      self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.yvel = 0 # скорость вертикального перемещения
   #     self.onGround = False # На земле ли я?
        self.image = Surface((WIDTH,HEIGHT))             #создаем поверхность и ниже заливаем цветом
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
        self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным
#        Анимация движения вправо
##########################################################################################
        boltAnim = []
        for anim in ANIMATION_RIGHT:#берем из кучи спрайтов 1
            boltAnim.append((anim, ANIMATION_DELAY))#добавляем его и скорость смены кадров
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)#используем спец библиотеку pyganim
        self.boltAnimRight.play()#запускаем весь движ
##########################################################################################  
#        Анимация движения влево        
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        
 
 
sc = pygame.display.set_mode((W, H))#
 
# координата x будет случайна
man1 = man(randint(1, W), 200)
 
while 1:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			sys.exit()
 
	sc.fill(WHITE)#закрасить фон
	sc.blit(man1.image, man1.rect)#нарисовать
	pygame.display.update()#обновить
	pygame.time.delay(20)#фпс
 
    # машинка ездит сверху вниз
'''	if car1.rect.y < H:
		car1.rect.y += 5
	else:
		car1 = Car(randint(1, W), '0.png')
		car1.rect.y = 0'''
		
