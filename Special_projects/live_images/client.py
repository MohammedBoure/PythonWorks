from server import MultiplayerClient
import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800 , 450

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def pixel(x,y,color):
    pygame.draw.rect(screen,color,(x,y,1,1))


running = True
client = MultiplayerClient("192.168.43.144")

def filter(x):
    num = 0
    list_of_data = []
    for i in x:
        if num == 2 and x != "":
            list_of_data.append(x[:3])
            x = x [3:]
            num = 0
        num += 1
    return list_of_data

while running:
    data = client.cycle_recv()
    for i in pygame.event.get():
        if type(i)==768:
            client.cycle_send("1")
    
    for i in data:
        pygame.draw.rect(screen,(i[2],i[3],i[4]),(i[0],i[1],1,1))
        pygame.display.flip()

pygame.quit()
sys.exit()

