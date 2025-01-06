import pygame
from pygame.locals import QUIT

pygame.init()

WHITE = (255,255,255)
X,Y = 800,600
surface = pygame.display.set_mode((X,Y))

while True:
    pygame.time.Clock().tick(10)
    surface.fill(WHITE)
    pygame.display.flip()
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
        if event:
            print(event)