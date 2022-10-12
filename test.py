import sys
import pygame
import time
animation_setR = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]
animation_setL = [pygame.image.load(f"l{i}.png") for i in range(1, 6)]
pygame.init()
s=0
screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(0, 0, 0, 0)
s = pygame.image.load("0.png")
x=311
y=447
animation_set = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
i = 0
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
