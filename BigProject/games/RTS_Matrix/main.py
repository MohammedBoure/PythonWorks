import pygame
import sys
from function import get_mouse_direction, draw_text


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Screen setup
WIDTH, HEIGHT = 1200 , 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Grid Strategy Game")

# Calculate initial grid size based on screen size
GRID_COLUMNS = 16
GRID_ROWS = 12
grid_size = min(WIDTH // GRID_COLUMNS, HEIGHT // GRID_ROWS)

class Unit:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, offset_x, offset_y, grid_size):
        pygame.draw.rect(screen, self.color, 
                         (self.x * grid_size + offset_x, self.y * grid_size + offset_y, grid_size, grid_size))

# Initialize units
units = [
    Unit(2, 2, BLUE),
    Unit(5, 5, RED)
]

# Offsets for grid movement
offset_x, offset_y = 0, 0

# Previous mouse position
prev_mouse_pos = None

running = True
while running:
    curr_mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                grid_x, grid_y = (pos[0] - offset_x) // grid_size, (pos[1] - offset_y) // grid_size
                units.append(Unit(grid_x, grid_y, BLUE))
            elif event.button == 4:  # Mouse wheel up
                grid_size += 5
            elif event.button == 5:  # Mouse wheel down
                grid_size = max(5, grid_size - 5)  # Ensure grid_size does not become too small
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                offset_x += grid_size
            elif event.key == pygame.K_RIGHT:
                offset_x -= grid_size
            elif event.key == pygame.K_UP:
                offset_y += grid_size
            elif event.key == pygame.K_DOWN:
                offset_y -= grid_size
        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            mouse_direction = get_mouse_direction(prev_mouse_pos, curr_mouse_pos, event)

    prev_mouse_pos = curr_mouse_pos

    screen.fill(WHITE)
    
    # Draw grid
    for x in range(0, WIDTH + grid_size, grid_size):
        pygame.draw.line(screen, BLACK, ((x + offset_x % grid_size), 0), ((x + offset_x % grid_size), HEIGHT))
    for y in range(0, HEIGHT + grid_size, grid_size):
        pygame.draw.line(screen, BLACK, (0, (y + offset_y % grid_size)), (WIDTH, (y + offset_y % grid_size)))
    
    # Draw units
    for unit in units:
        unit.draw(offset_x, offset_y, grid_size)
    
    # Draw offset values and grid size on the screen
    draw_text(screen, f"Offset Y: {offset_y}", (10, 10), 20, BLACK)
    draw_text(screen, f"Offset X: {offset_x}", (10, 40), 20, BLACK)
    draw_text(screen, f"Grid Size: {grid_size}", (10, 70), 20, BLACK)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
