from sockelab import MultiplayerClient
import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800 , 450

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def pixel(x,y,color):
    pygame.draw.rect(screen,color,(x,y,1,1))


running = True
client = MultiplayerClient("127.0.0.1")

def filter(x):
    num = 0
    list_of_data = []
    for i in x:
        if num == 2 and x != "":
            list_of_data.append(int(x[:3]))
            x = x [3:]
            num = 0
        num += 1
    return list_of_data

while running:              
    data = client.cycle_recv(15)
    data = filter(data)
    try:
        pygame.draw.rect(screen,(data[3],data[4],data[2]),(data[0],data[1],1,1))
    except:pass
    pygame.display.flip()
    
pygame.quit()
sys.exit()

