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

def tan(x):
    return math.sin(x)/math.cos(x)
def cos(x):
    return math.cos(x)
def sin(x):
    return math.sin(x)

def add_edge(num):
    edge = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),(0, 0, 1),(0, 0, -1)]  # ,(0,0,1),(0,0,-1)]
    list_x = []
    list_y = []
    for i in range(num):
        list_y.append((i+1)/(num+1))
        list_x.append((i+1)/(num+1))

    for x in list_x:
        y = (1-x**2)**(1/2)
        edge.append((x, y, 0))
        edge.append((x, -y, 0))
        edge.append((-x, -y, 0))
        edge.append((-x, y, 0))
    for x in list_y:
        y = (1-x**2)**(1/2)
        edge.append((0,x, y))
        edge.append((0,x, -y))
        edge.append((0,-x, -y))
        edge.append((0,-x, y))
    return edge

edge = add_edge(10)
x = 0



def Ry(x):
    a = cos(x)**2
    b = sin(x)**2
    return [[1,0,0],[0,1,cos(x)],[0,0,1]]

def Rx(x):
    a = cos(x)**2
    b = sin(x)**2
    return [[1,0,0],[0,1,0],[0,0,1]]



matrix_unit = [[1,0,0],[0,1,0],[0,0,1]]

def matrix_multiple4x2(a,b):
    x =a[0][0]*b[0]+a[0][1]*b[1]
    y =a[1][0]*b[0]+a[1][1]*b[1]
    return [x,y]

def matrix_multiple9x3(matrix_unit,matrix_b):
    a,b,c = matrix_unit[0]
    d,e,f = matrix_unit[1]
    g,h,i = matrix_unit[2]
    x,y,z = matrix_b
    x = a*x + b*y + c*z
    y = d*x + e*y + f*z
    z = g*x + h*y + i*z
    return [x,y,z]


running = True
speed = 0.01
while running:
    screen.fill(BLACK)
    matrix_unit = [[sin(x)**2,0,cos(x)**2],[0,1,0],[0,0,1]]

    for i in range(len(edge)):
        #time.sleep(1)
        #print(800/2+matrix_multiple9x3(matrix_unit,edge[i])[0]*60)
        #if i==7:
        #    print("------")
        pygame.draw.rect(screen,WHITE,(800/2 + matrix_multiple9x3(matrix_unit,edge[i])[0]*60,600/2+matrix_multiple9x3(Rx(x),edge[i])[1]*60,5,5))
        #pygame.display.flip()
    time.sleep(0.06)
    x += 0.2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
sys.exit()
