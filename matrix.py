def print_matrix(matrix):
    """ Print out a matrix nicely.
        Values in each column will be right-aligned.
        No borders or anything.
    """
    # Convert all values in the matrix to string type.
    # This is done so that we can use the len() function on each value.
    matrix2 = [list(map(str, row)) for row in matrix]
    
    # Transpose the matrix.
    # The rows in the transposed matrix correspond to the columns in the original matrix.
    matrix_T = list(zip(*matrix2))
    
    # Find the maximum width required for each column.
    cws = [max(map(len, col)) for col in matrix_T]
    
    # Now to actually print out the values.
    # r is the index for the outer list, corresponding to row number.
    # c is the index for the inner lists, corresponding to column number.
    for r in range(len(matrix2)):
        for c in range(len(matrix2[r])):
            # Calculate how many spaces to add in front of the value to make it right-aligned.
            pad = (cws[c] - len(matrix2[r][c])) * ' '
            
            # Print the values out, separated by a space ' '.
            print(pad + matrix2[r][c], end=' ')
        # Print a newline.
        print()

def matrix_multiply(left_matrix, right_matrix):
    # Perform conversions if the input format is not correct.
    # This is defensive programming.
    if not isinstance(left_matrix[0], (list, tuple)):
        """ If pre-multiplying with a row vector:
            Row vectors should be entered as [[a, b, c]].
            If entered as [a, b, c], then convert to the above.
        """
        left_matrix = [left_matrix]
    if not isinstance(right_matrix[0], (list, tuple)):
        """ If post-multiplying with a column vector:
            Column vectors should be entered as [[a], [b], [c]].
            If entered as [a, b, c], then convert to the above.
        """
        right_matrix = [[val] for val in right_matrix]
    
    # Declare a new matrix, of the correct size to store the result.
    # Set all initial values to 0, then we can increment/reassign later.
    new_matrix = []
    for r in range(len(left_matrix)):
        new_row = []
        for c in range(len(right_matrix[0])):
            new_row.append(0)
        new_matrix.append(new_row)
#     new_matrix = [[0 for c in range(len(right_matrix[0]))] for r in range(len(left_matrix))]
    
    # First 2 loops scan through the new_matrix, 1 cell at a time.
    # We are essentially calculating the result, 1 cell at a time.
    for r in range(len(new_matrix)):
        for c in range(len(new_matrix[r])):
            # This is the dot product of the r-th row of left_matrix and c-th column of right-matrix.
            for i in range(len(right_matrix)):
                new_matrix[r][c] += left_matrix[r][i] * right_matrix[i][c]
    return new_matrix

A = [[1, 2, 3],
     [4, 5, 6]]
B = [[1],
     [2],
     [3]]
# A = [1, 2, 3]
# B = [1, 2, 3]
print_matrix(matrix_multiply(A, B))
print()
print_matrix(matrix_multiply(B, A))
print_matrix(matrix_multiply(B, [5]))
