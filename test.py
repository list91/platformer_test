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
'''
btn=True 
while btn:
	t=pygame.time.Clock()
	t.tick(11)
	screen.blit(s, (x, y))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
	keys=pygame.key.get_pressed()
	#if keys[pygame.K_DOWN]:
			#y+=1
	if keys[pygame.K_LEFT]:
			x-=1
	elif keys[pygame.K_RIGHT]:
		
		screen.blit(animation_set[i // 12], (x, y))
		i+=1
		if i ==60:
			i=0
		
		#for i in range(1,6):
			#x+=1
			#s=pygame.image.load(f"r{i}.png")
			#screen.blit(i,(x,y))
			
	#if keys[pygame.K_UP]:
			#y-=1
	elif keys[pygame.K_SPACE]:
			print(animation_set)
			print(s)
	else:
		s = pygame.image.load("0.png")
	screen.fill((0, 0, 0))#очистить остатки
	#screen.blit(s, (x, y))
	i=0
	screen.blit(animation_set[i // 12], (x, y))
	i+=1
	if i ==60:
		i=0
	#pygame.draw.rect(screen, (255, 0, 0), rect, 0)

	pygame.display.flip()#обновить окно
	
pygame.quit()
'''
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
        #window.fill((0, 0, 0))
    
    
    pygame.display.flip()
    window.fill((0, 0, 0))
    clock.tick(100)
