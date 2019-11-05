from typing import List, Tuple

Point = Tuple[int, int]

def paths_to_xy(x: int, y: int, in_pts: List[Point]=[]) -> int:
    """ Number of shortest paths to a point is the sum of the number of 
        shortest paths to its parent points. 
        
        Exception:
            There is only 1 shortest path to any point along the edges 
            containing the origin.
        
        No paths can travel through inner grid points, so if a parent point 
        happens to be an inner grid point, it contributes 0 paths to the sum.
        
        Arguments:
            x (int): final row
            y (int): final column
            in_pts (list of tuples): list of inner grid points
        
        Return the number of allowed paths from (0, 0) to (x, y).
    """
    if (x, y) in in_pts:
        return 0
    elif x < 1 or y < 1:
        return 1
    else:
        return paths_to_xy(x - 1, y, in_pts) + paths_to_xy(x, y - 1, in_pts)

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
    elif (inX < 0) or (sizeGrid <= inX):
        print('Error: Inner grid origin cannot be at the top or right edges.')
    elif sizeGrid < inX + inSize:
        print('Error: Inner grid must be within the main grid.')
    else:
        return True
    return False

def nsp(sizeGrid: int, inX: int, inSize: int) -> int:
    """ Calculate the number of allowed shortest paths from (0, 0) to (n, n), 
        where n = sizeGrid - 1, avoiding all points in an inner grid starting 
        at (inX, inX) with a size of inSize.
        
        Arguments:
            sizeGrid (int): size of the main grid
            inX (int): coordinates of the bottom-left corner of the inner grid
            inSize (int): size of the inner grid
        
        Return the number of paths.
    """
    if valid_input(sizeGrid, inX, inSize):
        final_x = sizeGrid - 1
        final_y = sizeGrid - 1
        forbidden_points = get_forbidden_points(inX, inX, inSize, inSize)
        return paths_to_xy(final_x, final_y, in_pts=forbidden_points)
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
        'nsp(-2, 1, 3)', # error
        'nsp(2, 1, 3)', # error
        'nsp(6, 6, 3)', # error
    #     'nsp("a", 1, 3)', # maybe next time...
    ]

    for test in tests:
        print(test)
        print(eval(test))
