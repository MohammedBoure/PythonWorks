import pygame
from game import Game
from constants import WHITH, SCREEN_WIDTH,SCREEN_HEIGHT,FPS

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()


running = True
screen.fill(WHITH)
game = Game(screen)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game.handle_event(event)
        
    game.circle()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
