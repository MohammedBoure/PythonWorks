import pygame
import sys
import time
from random import randint

pygame.init()


width = 800
height = 600

size = pygame.display.get_desktop_sizes()

screen = pygame.display.set_mode((width,height))

WHITE = (255, 255, 255)
BLACK = (0,0,0)

list_y = []
for i in range(201):
    list_y.append(0)



def carre():
    list_x =[]
    x = 0
    for i in range(201):
        list_x.append(x)
        x += 4
    return list_x

running = True
while running:
    x = randint(0,200)
    max_y = max(list_y)

    if x!=200 and ((abs(list_y[x+1]-list_y[x])<=12 and abs(list_y[x-1]-list_y[x])<=12) or list_y[x]<max_y-100 or x>150):
        list_y[x] += 4
    screen.fill(BLACK)
    #time.sleep(0.06)
    for i in range(200):
        pygame.draw.rect(screen,WHITE,(carre()[i],0,4,600-list_y[i]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
