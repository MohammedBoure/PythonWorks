import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP

pygame.init()

WHITE = (255, 255, 255)
X, Y = 800, 600
surface = pygame.display.set_mode((X, Y))

running = True
while running:
    pygame.time.Clock().tick(10)
    surface.fill(WHITE)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            print(type(event.unicode))
        elif event.type == KEYUP:
            print(event.unicode)

pygame.quit()
