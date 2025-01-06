import pygame
import sys
import screeneshot

pygame.init()


WIDTH, HEIGHT = 800 , 450

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def pixel(x,y,color):
    pygame.draw.rect(screen,color,(x,y,1,1))



running = True
data =  screeneshot.screnshot_pixel()
while running:
    
    for i in data:
        pygame.draw.rect(screen,i[1],(i[0][0],i[0][1],1,1))
        pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()