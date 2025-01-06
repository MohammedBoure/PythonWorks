import pygame

def draw_text(screen, text, position, font_size, color):
    """
    Draws text on the screen at the specified position with the given font size and color.

    Parameters:
    - screen: The Pygame screen surface.
    - text: The text to be displayed.
    - position: A tuple (x, y) representing the position to draw the text.
    - font_size: The size of the font.
    - color: The color of the text.
    """
    font = pygame.font.Font(None, font_size)
    # Render the text
    text_surface = font.render(text, True, color)
    # Get the rect of the text surface
    text_rect = text_surface.get_rect()
    # Set the position of the rect
    text_rect.topleft = position
    # Draw the text surface on the screen
    screen.blit(text_surface, text_rect)




def get_mouse_direction(prev_pos, curr_pos, mouse_event):
    """
    Returns the direction of the mouse movement or wheel movement.

    Parameters:
    - prev_pos: A tuple (x, y) representing the previous position of the mouse.
    - curr_pos: A tuple (x, y) representing the current position of the mouse.
    - mouse_event: The pygame mouse event.

    Returns:
    - An integer representing the direction:
      - 0: No movement
      - 1: Right
      - -1: Left
      - 2: Down
      - -2: Up
      - 3: Wheel up
      - -3: Wheel down
    """
    if mouse_event.type == pygame.MOUSEBUTTONDOWN:
        if mouse_event.button == 4:  # Wheel up
            return 1.1
        elif mouse_event.button == 5:  # Wheel down
            return -1.1

    if prev_pos is None:
        return 1

    dx = curr_pos[0] - prev_pos[0]
    dy = curr_pos[1] - prev_pos[1]

    if abs(dx) > abs(dy):
        if dx > 0:
            return 1
        elif dx < 0:
            return -1
    else:
        if dy > 0:
            return 1.2
        elif dy < 0:
            return -1.2

    return 0


