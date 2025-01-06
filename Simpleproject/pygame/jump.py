import pygame
import math

pygame.init()



def rect(color,pos_x,pos_y,width,height):
        pygame.draw.rect(screen,color,(pos_x,pos_y,width,height))


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))



WHITHE = (255, 255, 255)
BLACK = (0,0,0)
clock = pygame.time.Clock()
fps = 75
screen.fill(WHITHE)
running = True
pos_y = 500
val = False
x = -math.pi
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == 768 and  event.key == 32:
            val = True
            x = -math.pi


    if x < math.pi and val:
         pos_y = 10 * x + pos_y
         x += 0.2

    rect(BLACK,100,pos_y,50,50)
    
         
         
    screen.fill(WHITHE)
    rect(BLACK,400,pos_y,50,50)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()







#<Event(768-KeyDown {'unicode': ' ', 'key': 32, 'mod': 4096, 'scancode': 44, 'window': None})>
