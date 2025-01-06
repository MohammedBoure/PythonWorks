def array(pos:tuple, mod:int):
    """
    This function returns the coordinates of a rectangle based on the position (pos) and the modification type (mod).

    Parameters:
    pos : tuple
        A pair of values representing the position coordinates (x, y).
    mod : int
        A numerical value that determines the type of modification:
        - If the value is 1, the function returns the coordinates of a horizontal rectangle.
        - If the value is 2, the function returns the coordinates of a vertical rectangle.

    Returns:
    tuple
        The coordinates of the rectangle in the form (x, y, width, height):
        - If mod = 1, the return value is (x*40 - 40, y*40 - 10, 40, 10).
        - If mod = 2, the return value is (x*40 - 10, y*40 - 40, 10, 40).

    Examples:
    >>> array((2, 3), 1)
    (40, 110, 40, 10)
    >>> array((2, 3), 2)
    (70, 80, 10, 40)
    """
    if mod == 1:
        return (pos[0]*40-40, pos[1]*40-10, 40, 10)
    if mod == 2:
        return (pos[0]*40-10, pos[1]*40-40, 10, 40)

    
def dearray(pos:tuple):
    """
    This function converts the coordinates of a rectangle back to its original position.

    Parameters:
    pos : tuple
        A pair of values representing the coordinates (x, y).

    Returns:
    tuple
        The original position coordinates in the form (x, y):
        - The return value is (x//40 + 1, y//40 + 1).

    Examples:
    >>> dearray((80, 120))
    (3, 4)
    >>> dearray((40, 40))
    (2, 2)
    """
    return (pos[0]//40 + 1, pos[1]//40 + 1)

    
def array_circle(pos:tuple):
    return pos[0]*40-25,pos[1]*40-24



def point_in_rect(rect:tuple, point:tuple):
    """
    This function checks if a given point is inside a specified rectangle.

    It performs the following steps:
    1. Extracts the coordinates and dimensions of the rectangle.
    2. Extracts the coordinates of the point.
    3. Checks if the point lies within the bounds of the rectangle.

    Parameters:
    rect : tuple
        A tuple containing the coordinates and dimensions of the rectangle (x, y, width, height).
    point : tuple
        A tuple containing the coordinates of the point (x, y).

    Returns:
    bool
        Returns True if the point is inside the rectangle, otherwise returns False.

    Examples:
    >>> point_in_rect((10, 10, 50, 50), (30, 30))
    True
    >>> point_in_rect((10, 10, 50, 50), (70, 70))
    False
    """
    x, y, dx, dy = rect
    xp, yp = point
    if x < xp < x + dx and y < yp < y + dy:
        return True
    else:
        return False
    
    
def is_line_intersect_square(x1, y1, x2, y2, square):
    """
    This function checks if a line segment intersects with a given square.

    It performs the following steps:
    1. Defines a helper function `line_intersects_line` to check if two line segments intersect.
    2. Creates a list of line segments representing the edges of the square.
    3. Checks if the given line segment intersects with any of the square's edges.

    Parameters:
    x1, y1 : float
        The coordinates of the first point of the line segment.
    x2, y2 : float
        The coordinates of the second point of the line segment.
    square : tuple
        A tuple containing the coordinates and dimensions of the square (x, y, width, height).

    Returns:
    bool
        Returns True if the line segment intersects with the square, otherwise returns False.

    Examples:
    >>> is_line_intersect_square(0, 0, 10, 10, (5, 5, 10, 10))
    True
    >>> is_line_intersect_square(0, 0, 4, 4, (5, 5, 10, 10))
    False
    """
    def line_intersects_line(p0, p1, p2, p3):
        s1_x = p1[0] - p0[0]
        s1_y = p1[1] - p0[1]
        s2_x = p3[0] - p2[0]
        s2_y = p3[1] - p2[1]

        denominator = (-s2_x * s1_y + s1_x * s2_y)
        if denominator == 0:
            return False  

        s = (-s1_y * (p0[0] - p2[0]) + s1_x * (p0[1] - p2[1])) / denominator
        t = ( s2_x * (p0[1] - p2[1]) - s2_y * (p0[0] - p2[0])) / denominator

        return 0 <= s <= 1 and 0 <= t <= 1

    square_lines = [
        ((square[0], square[1]), (square[0] + square[2], square[1])),
        ((square[0], square[1]), (square[0], square[1] + square[3])),
        ((square[0] + square[2], square[1]), (square[0] + square[2], square[1] + square[3])),
        ((square[0], square[1] + square[3]), (square[0] + square[2], square[1] + square[3]))
    ]

    for line in square_lines:
        if line_intersects_line((x1, y1), (x2, y2), line[0], line[1]):
            return True

    return False





    
    



    
    
