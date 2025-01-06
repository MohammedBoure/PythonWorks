import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)

list_data = [random.randint(1, 100) for _ in range(400)]
list_data_org = []

max_num = max(list_data)
num_of_mul = height // max_num
dx = width // len(list_data)

for i in list_data:
    list_data_org.append(i * num_of_mul)

speed = 0

def bubble_sort_and_draw():
    n = len(list_data_org)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_data_org[j] > list_data_org[j + 1]:
                list_data_org[j], list_data_org[j + 1] = list_data_org[j + 1], list_data_org[j]
                
                draw_bars()

                pygame.time.delay(speed)

def draw_bars():
    screen.fill(white)  
    for index, value in enumerate(list_data_org):
        pygame.draw.rect(screen, black, (index * dx, height - value, dx - 1, value))
    pygame.display.flip() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bubble_sort_and_draw()

pygame.quit()
