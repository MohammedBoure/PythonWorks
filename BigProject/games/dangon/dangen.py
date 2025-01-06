import pygame
from random import randint
from function import array,dearray,array_circle


def first_creation():
    for i in range(21):
        for j in range(16):
            data = array((i,j),randint(1,2))
            pygame.draw.rect(screen,BLACK,data)
            list_of_data.append(data)

                    
    for i in range(21):
        pygame.draw.rect(screen,BLACK,array((i,0),1))
        pygame.draw.rect(screen,BLACK,array((i,15),1))
        list_of_walls_rect.append(array((i,15),1))
        list_of_walls_rect.append(array((i,0),1))
    for i in range(16):
        pygame.draw.rect(screen,BLACK,array((0,i),2))
        pygame.draw.rect(screen,BLACK,array((20,i),2))
        list_of_walls_rect.append(array((0,i),2))
        list_of_walls_rect.append(array((20,i),2))
            
    pygame.draw.rect(screen,WHITH,array((20,7),2))
    pygame.draw.line(screen,BLACK,(0,0),(0,600),15)
    pygame.draw.line(screen,BLACK,(0,0),(800,0),15)
    x,y,dx,dy = array((0,7),2)
    pygame.draw.rect(screen,WHITH,(x + 10,y,dx,dy))
    pygame.draw.rect(screen,WHITH,array((10,7),1))
    pygame.draw.rect(screen,WHITH,array((10,7),2))
    


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITH = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
clock = pygame.time.Clock()
fps = 40
screen.fill(WHITH)
running = True
list_of_data = []
list_of_walls_rect = []


first_creation()
button_left = 0
print(array_circle((9,6)))
x_circle,y_circel = (380, 260)
while running:
    pygame.draw.circle(screen, RED, (x_circle,y_circel), 10)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == 1025 and event.button == 3:
            button_left += 1
            if button_left % 2 == 0:
                
                if array(dearray(event.pos),2) in list_of_data:
                    pygame.draw.rect(screen,BLACK,array(dearray(event.pos),2))
                    print(array(dearray(event.pos),2))
                else:
                    pygame.draw.rect(screen,WHITH,array(dearray(event.pos),2))
                pygame.draw.rect(screen,RED,array(dearray(event.pos),1))
            elif button_left % 3 == 0:
                
                if array(dearray(event.pos),1) in list_of_data:
                    pygame.draw.rect(screen,BLACK,array(dearray(event.pos),1))
                else:
                    pygame.draw.rect(screen,WHITH,array(dearray(event.pos),1))
                pygame.draw.rect(screen,RED,array(dearray(event.pos),2))
            else:
                if array(dearray(event.pos),1) in list_of_data:
                    pygame.draw.rect(screen,BLACK,array(dearray(event.pos),1))
                else:
                    pygame.draw.rect(screen,WHITH,array(dearray(event.pos),1))
                if array(dearray(event.pos),2) in list_of_data:
                    pygame.draw.rect(screen,BLACK,array(dearray(event.pos),2))
                    print(array(dearray(event.pos),2))
                else:
                    pygame.draw.rect(screen,WHITH,array(dearray(event.pos),2))
                
            if button_left == 3:
                button_left = 0
                    
                
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit

"""<Event(1025-MouseButtonDown {'pos': (3, 3), 'button': 3, 'touch': False, 'window': None})>
<Event(1026-MouseButtonUp {'pos': (3, 3), 'button': 3, 'touch': False, 'window': None})>
<Event(1025-MouseButtonDown {'pos': (5, 3), 'button': 1, 'touch': False, 'window': None})>
<Event(1026-MouseButtonUp {'pos': (5, 3), 'button': 1, 'touch': False, 'window': None})>"""