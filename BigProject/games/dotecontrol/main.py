import pygame
from game import Game
from constants import WHITH, SCREEN_WIDTH,SCREEN_HEIGHT,FPS

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()


running = True
screen.fill(WHITH)
game = Game(screen)
game.first_creation()
num_cicle = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game.event(event)
    game.cicle()
    pygame.display.flip()
    clock.tick(FPS)
    num_cicle += 1
    game.recv_data(1)
    if num_cicle == FPS:
        num_cicle = 0

pygame.quit()
