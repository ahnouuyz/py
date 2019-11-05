from typing import List, Tuple

Point = Tuple[int, int]

def steps_to_xy(x: int, y: int, forbidden: List[Point]=[]) -> int:
    """ The number of steps to get to a certain point is simply the 
        sum of the number of steps to reach the previous two points, 
        unless one of the "previous points" is "outside" the board 
        (does not exist), in which case "it" contributes 0 (the other 
        point contributes as per normal). 
        
        The origin always contributes 1.
        
        Forbidden points, if any, are points on the inner grid, 
        and contribute 0.
        
        Arguments:
            x (int): final row
            y (int): final column
            forbidden (list of tuples): list of points that the path cannot cross
        
        Return the number of allowed paths from (0, 0) to (x, y).
    """
    if (x, y) in forbidden:
        return 0
    elif x < 1 and y < 1:
        return 1
    elif x < 1:
        return steps_to_xy(x, y - 1, forbidden)
    elif y < 1:
        return steps_to_xy(x - 1, y, forbidden)
    else:
        return steps_to_xy(x - 1, y, forbidden) + steps_to_xy(x, y - 1, forbidden)

def get_forbidden_points(x0: int, y0: int, dx: int, dy: int) -> List[Point]:
    """ Create a list of points covered by the inner grid. These will be the 
        forbidden points which the path cannot cross.
        
        Arguments:
            x0 (int): bottom-most coordinate of the inner grid
            y0 (int): left-most coordinate of the inner grid
            dx (int): vertical size of the inner grid
            dy (int): horizontal size of the inner grid
        
        Return the list of forbidden points.
    """
    return [(i, j) for i in range(x0, x0 + dx) for j in range(y0, y0 + dy)]

def valid_input(sizeGrid: int, inX: int, inSize: int) -> bool:
    if sizeGrid < 0:
        print('Error: Main grid must have positive size.')
        return False
    elif (inX < 0) or (sizeGrid <= inX):
        print('Error: Inner grid origin cannot be at the top or right edges.')
        return False
    elif sizeGrid < inX + inSize:
        print('Error: Inner grid must be within the main grid.')
        return False
    else:
        return True

def nsp(sizeGrid: int, inX: int, inSize: int) -> int:
    """ Calculate the number of allowed shortest paths from (0, 0) to (n, n), 
        where n = sizeGrid - 1, avoiding all points in an inner grid starting 
        at (inX, inX) with a size of inSize.
        
        Arguments:
            sizeGrid (int): size of the main grid
            inX (int): coordinates (repeated) of the bottom-left corner of the inner grid
            inSize (int): size of the inner grid
        
        Return the number of paths.
    """
    if valid_input(sizeGrid, inX, inSize):
        final_x = sizeGrid - 1
        final_y = sizeGrid - 1
        forbidden_points = get_forbidden_points(inX, inX, inSize, inSize)
        return steps_to_xy(final_x, final_y, forbidden=forbidden_points)
    else:
        print('  Execution failed with the following parameters:')
        print(f'{"SizeGrid: " + str(sizeGrid):>16}')
        print(f'{"inX: " + str(inX):>16}')
        print(f'{"inSize: " + str(inSize):>16}')

if __name__ == '__main__':
    tests = [
        'nsp(5, 1, 3)', # 2
        'nsp(2, 0, 0)', # 2
        'nsp(5, 0, 1)', # 0
        'nsp(5, 4, 1)', # 0
        'nsp(5, 2, 0)', # 70
        'nsp(-2, 1, 3)',
        'nsp(2, 1, 3)',
        'nsp(6, 6, 3)',
    #     'nsp("a", 1, 3)',
    ]

    for test in tests:
        print(test)
        print(eval(test))
