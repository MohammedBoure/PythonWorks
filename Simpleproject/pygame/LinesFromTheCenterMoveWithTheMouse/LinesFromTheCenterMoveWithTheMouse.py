import pygame
import sys
import math
import time
pygame.init()

width = 800
height = 600

size = pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((width,height))

WHITE = (255, 255, 255)
BLACK = (0,0,0)

def cos(x):
    return math.cos(x)
def sin(x):
    return math.sin(x)

z = 0


def draw_vectore(x,y):
    return (800/2 + x*20,600/2 + y*20)

def multi_vectore(vec,a):
    return (vec[0]*a,vec[1]*a)

def add_vectore_and_vectore(vec1,vec2):
    return (vec1[0]+vec2[0],vec1[1]+vec2[1])

def base_create_vectore(x,y,acc):
    num = 360 / acc
    num2 = 0
    while num2<360:
        vec = multi_vectore((cos(num2),sin(num2)),800)
        pygame.draw.line(screen,WHITE,(x,y),
                         add_vectore_and_vectore(vec,(x,y)),1)
        num2 += num

def shows(index):
    x,y = index
    return ((x-800/2)/20,(y-600/2)/20)

running = True
speed = 0.01

x = 2
y = 2
while running:
    screen.fill(BLACK)
    matrix_unit = [[sin(x)**2,0],[0,1,0]]
    pygame.draw.rect(screen,WHITE,(800/2 + x*15,600/2 + y*20,1,2))
    base_create_vectore(800/2 + x*15, 600/2 + y*20,20)
    z += 0.2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 1024:
            x,y = shows(event.pos)
            print(x,y)
    pygame.display.flip()

pygame.quit()
sys.exit()
