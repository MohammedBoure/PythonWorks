import pygame
from random import randint
from function import array, dearray,array_circle,is_line_intersect_square
from constants import BLACK, WHITH, RED , BLUE

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.list_of_data = []
        self.list_of_data2 = []
        self.button_left = 0
        self.circle1 = [array_circle((10,1))[0], array_circle((10,1))[1]]
        self.circle2 = [array_circle((10,15))[0],array_circle((10,15))[1]]
        self.first_creation()
        self.a,self.b = False,False
        self.button_is_press = False
        self.motion_pos = (0,0)
        
        
    def circle(self):
        s1_x = self.circle1[0]
        s1_y = self.circle1[1]
        s2_x = array_circle(dearray(self.motion_pos))[0]
        s2_y = array_circle(dearray(self.motion_pos))[1]
        pygame.draw.circle(self.screen, RED, (self.circle1[0], self.circle1[1]), 7)
        pygame.draw.circle(self.screen, BLUE, (self.circle2[0], self.circle2[1]), 7)
        if self.button_is_press:
            self.is_line_intersect_square_is_Treu = True
            for i in self.list_of_data:
                if (is_line_intersect_square(s1_x,s1_y,s2_x,s2_y,i)):   #s1_x,s1_y,s2_x,s2_y
                    self.is_line_intersect_square_is_Treu = False
                    break
            if self.is_line_intersect_square_is_Treu:
                pygame.draw.line(self.screen,RED,(s1_x,s1_y),(s2_x,s2_y),3)


    def first_creation(self):
        """
        This function initializes the game screen by drawing rectangles and lines to create the initial layout.

        It performs the following steps:
        1. Draws random rectangles within a 21x16 grid and stores their coordinates in `self.list_of_data`.
        2. Draws horizontal boundary rectangles at the top and bottom of the grid and stores their coordinates in `self.list_of_data`.
        3. Draws vertical boundary rectangles on the left and right sides of the grid and stores their coordinates in `self.list_of_data`.
        4. Draws specific white rectangles and lines to create designated areas on the screen.

        Parameters:
        None

        Returns:
        None

        Examples:
        >>> self.first_creation()
        # This will draw the initial layout on the game screen.
        """
        for i in range(21):
            for j in range(16):
                data = array((i, j), randint(1, 2))
                if not (data == array((20,7),2) or data == array((0,7),2)):
                    pygame.draw.rect(self.screen, BLACK, data)
                    self.list_of_data.append(data)

        for i in range(21):
            pygame.draw.rect(self.screen, BLACK, array((i, 0), 1))
            pygame.draw.rect(self.screen, BLACK, array((i, 15), 1))
            self.list_of_data2.append(array((i, 15), 1))
            self.list_of_data2.append(array((i, 0), 1))
        for i in range(16):
            if not (data == array((20,7),2) or data == array((0,7),2)):
                pygame.draw.rect(self.screen, BLACK, array((0, i), 2))
                pygame.draw.rect(self.screen, BLACK, array((20, i), 2))
                self.list_of_data2.append(array((0, i), 2))
                self.list_of_data2.append(array((20, i), 2))

        pygame.draw.rect(self.screen, WHITH, array((20, 7), 2))
        pygame.draw.line(self.screen, BLACK, (0, 0), (0, 600), 15)
        pygame.draw.line(self.screen, BLACK, (0, 0), (800, 0), 15)
        x, y, dx, dy = array((0, 7), 2)
        pygame.draw.rect(self.screen, WHITH, (x + 10, y, dx, dy))



    def handle_event(self, event):
        """
        This function handles various events on the game screen, such as mouse button clicks and key presses.

        It performs the following steps:
        1. Checks if the event is a right mouse button click and calls `handle_mouse_button3`.
        2. Checks if the event is a key press and calls `handle_key_press`.

        Parameters:
        event : pygame.event.Event
            The event object containing information about the event.

        Returns:
        None

        Examples:
        >>> self.handle_event(event)
        # This will handle the event based on its type.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            self.handle_mouse_button3(event)
        elif event.type == pygame.KEYDOWN:
            self.handle_key_press(event)
        elif (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.MOUSEBUTTONUP) and event.button == 1:
            self.handle_mouse_button1(event)
        elif event.type == pygame.MOUSEMOTION:
            self.handle_mouse_motion(event)
            
    
    def handle_mouse_button1(self,event):
        self.pos = event.pos
        print(dearray(self.pos),dearray(self.circle1))
        if dearray(self.pos) == dearray(self.circle1) or dearray(self.pos) == dearray(self.circle2): 
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(11111111)
                self.button_is_press = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.button_is_press = False
                
                
    def handle_mouse_motion(self,event):
        self.motion_pos = event.pos

                
        print(dearray(self.motion_pos))
        


    def handle_mouse_button3(self, event):
        """
        This function handles right mouse button click events.

        It performs the following steps:
        1. Increments the `button_left` counter.
        2. Converts the mouse position to grid coordinates using `dearray`.
        3. Updates the state and draws rectangles based on the number of clicks.
        4. Resets the click counter after three clicks.

        Parameters:
        event : pygame.event.Event
            The event object containing information about the mouse event.

        Returns:
        None

        Examples:
        >>> self.handle_mouse_button3(event)
        # This will handle the right mouse button click event.
        """
        self.button_left += 1
        pos = dearray(event.pos)
        if self.button_left % 2 == 0:
            self.update_state(pos, 2, array(pos, 1), True, False)
        elif self.button_left % 3 == 0:
            self.update_state(pos, 1, array(pos, 2), False, True)
        else:
            self.toggle_rect(pos, 1)
            self.toggle_rect(pos, 2)
            self.reload_map()
            self.a, self.b = False, False

        if self.button_left == 3:
            self.button_left = 0


    def handle_key_press(self, event):
        """
        This function handles key press events.

        It performs the following steps:
        1. Checks if the 's' key is pressed and calls `remove_data`.
        2. Checks if the 'd' key is pressed and calls `add_data`.

        Parameters:
        event : pygame.event.Event
            The event object containing information about the key press event.

        Returns:
        None

        Examples:
        >>> self.handle_key_press(event)
        # This will handle the key press event.
        """
        if event.key == pygame.K_s:
            self.remove_data()
        elif event.key == pygame.K_d:
            self.add_data()


    def update_state(self, pos:tuple, rect_type:int, place:tuple, a_state:bool, b_state:bool):
        """
        This function updates the state of the game based on the mouse click position and type of rectangle.

        It performs the following steps:
        1. Toggles the rectangle at the given position and type.
        2. Draws a red rectangle at the specified place.
        3. Updates the state variables `a` and `b`.

        Parameters:
        pos : tuple
            A pair of values representing the position coordinates (x, y).
        rect_type : int
            A numerical value that determines the type of rectangle.
        place : tuple
            The coordinates of the rectangle to be drawn.
        a_state : bool
            The state of the `a` variable.
        b_state : bool
            The state of the `b` variable.

        Returns:
        None

        Examples:
        >>> self.update_state((2, 3), 1, (40, 60, 40, 10), True, False)
        # This will update the state based on the given parameters.
        """
        self.toggle_rect(pos, rect_type)
        pygame.draw.rect(self.screen, RED, place)
        self.a, self.b = a_state, b_state
        if a_state:
            self.place_a = place
        if b_state:
            self.place_b = place


    def remove_data(self):
        """
        This function removes specific rectangles from the list of data and reloads the map.

        It performs the following steps:
        1. Removes `place_a` from `self.list_of_data` if `a` is True.
        2. Removes `place_b` from `self.list_of_data` if `b` is True.
        3. Calls `reload_map` to redraw the map.

        Parameters:
        None

        Returns:
        None

        Examples:
        >>> self.remove_data()
        # This will remove specific rectangles from the list of data.
        """
        if self.a and self.place_a in self.list_of_data:
            self.list_of_data.remove(self.place_a)
            pygame.draw.rect(self.screen,WHITH,self.place_a)
            self.reload_map()
        if self.b and self.place_b in self.list_of_data:
            pygame.draw.rect(self.screen,WHITH,self.place_b)
            self.list_of_data.remove(self.place_b)
            self.reload_map()


    def add_data(self):
        """
        This function adds specific rectangles to the list of data and draws them on the screen.

        It performs the following steps:
        1. Adds `place_a` to `self.list_of_data` and draws it if `a` is True.
        2. Adds `place_b` to `self.list_of_data` and draws it if `b` is True.

        Parameters:
        None

        Returns:
        None

        Examples:
        >>> self.add_data()
        # This will add specific rectangles to the list of data.
        """
        if self.a:
            self.list_of_data.append(self.place_a)
            pygame.draw.rect(self.screen, BLACK, self.place_a)
        if self.b:
            self.list_of_data.append(self.place_b)
            pygame.draw.rect(self.screen, BLACK, self.place_b)


    def reload_map(self):
        """
        This function redraws all the rectangles stored in the list of data on the screen.

        It performs the following steps:
        1. Iterates through `self.list_of_data` and draws each rectangle in black.

        Parameters:
        None

        Returns:
        None

        Examples:
        >>> self.reload_map()
        # This will redraw all the rectangles on the screen.
        """
        for data in self.list_of_data:
            pygame.draw.rect(self.screen, BLACK, data)
            
        pygame.draw.rect(self.screen, WHITH, array((20, 7), 2))
        pygame.draw.line(self.screen, BLACK, (0, 0), (0, 600), 15)
        pygame.draw.line(self.screen, BLACK, (0, 0), (800, 0), 15)
        x, y, dx, dy = array((0, 7), 2)
        pygame.draw.rect(self.screen, WHITH, (x + 10, y, dx, dy))



    def toggle_rect(self, pos:tuple, value:int):
        """
        This function toggles the color of a rectangle at a given position.

        It performs the following steps:
        1. Checks if the rectangle at the given position and value is in `self.list_of_data`.
        2. If it is, it draws the rectangle in black.
        3. If it is not, it draws the rectangle in white.

        Parameters:
        pos : tuple
            A pair of values representing the position coordinates (x, y).
        value : int
            A numerical value that determines the type of rectangle.

        Returns:
        None

        Examples:
        >>> self.toggle_rect((2, 3), 1)
        # This will toggle the rectangle at position (2, 3) with value 1.
        """
        if array(pos, value) in self.list_of_data:
            pygame.draw.rect(self.screen, BLACK, array(pos, value))
        else:
            pygame.draw.rect(self.screen, WHITH, array(pos, value))

