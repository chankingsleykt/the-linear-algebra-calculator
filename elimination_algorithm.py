def scale_row (i: list[float], scalar: float) -> None:
    """
    Given a row i in a matrix, scale each entry by scalar.

    Precondition: scalar != 0

    >>> a = [4.5, 3, 0.9]
    >>> scale_row(a, 2)
    >>> a
    [9.0, 6, 1.8]
    >>> a = [-1, 3.1, -0.5, 5]
    >>> scale_row(a, -3)
    >>> a
    [3, -9.3, 1.5, -15]
    >>> a = [-2]
    >>> scale_row(a, 0.5)
    >>> a
    [-1.0]
    >>> a = []
    >>> scale_row(a, 8)
    >>> a
    []

    """

    for entry in range(len(i)):
        i[entry]*=scalar


def scale_and_add_row (i: list[float], j: list[float], scalar: float) -> None:
    """
    Given rows i and j in a matrix, scale i by scalar and add to j.

    Precondition: len(i) == len(j), scalar != 0

    >>> a = [4, 3, 2]
    >>> b = [1, 1, 1]
    >>> scale_and_add_row(a, b, 2)
    >>> b
    [9, 7, 5]
    >>> a
    [4.0, 3.0, 2.0]
    >>> a = [-1, 3.1, -0.5, 5]
    >>> b = [2, 2, 1, 3]
    >>> scale_and_add_row(b, a, -3)
    >>> a
    [-7, -2.9, -3.5, -4]
    >>> b
    [2.0, 2.0, 1.0, 3.0]
    >>> a = [-2]
    >>> b = [100]
    >>> scale_and_add_row(b, a, 0.01)
    >>> a
    [-1.0]
    >>> b
    [100.0]
    >>> a = []
    >>> b = []
    >>> scale_and_add_row(a, b, 8)
    >>> a
    []
    >>> b
    []

    """

    scale_row(i, scalar)
    for entry in range(len(j)):
        j[entry] += i[entry]
        if j[entry] == 0: # handles case of -0.0 in Python
            j[entry] = abs(j[entry])
    scale_row(i, (1/scalar))


def switch_row (matrix: list[list[float]], i: int, j: int) -> None:
    """
    Given a list of list of floats matrix, switch row i with row j.

    Precondition: 0 <= i, j, <= len(matrix)
    >>> matrix = [[1, 0], [0, 1]]
    >>> switch_row(matrix, 0, 1)
    >>> matrix
    [[0, 1], [1, 0]]
    >>> matrix = [[1, 0], [0, 1], [2, 1], [3, 1]]
    >>> switch_row(matrix, 0, 2)
    >>> matrix
    [[2, 1], [0, 1], [1, 0], [3, 1]]

    """
   
    c = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = c


def find_leading_coefficient_row (matrix: list[list[float]], placed_rows: list[int], column: int) -> None:
    """
    Given a list of list of floats matrix, find the index of the first row
    not in placed_rows with a non-zero coefficient in column column. Return -1
    if there is no coefficient in that column. 

    Precondition: 0 <= column <= len(matrix)
    >>> matrix = [[0, 0, 2], [0, 10, 0], [1, 0, 0]]
    >>> find_leading_coefficient_row(matrix, [], 0)
    2
    >>> matrix = [[0, 0, 2], [0, 10, 0], [1, 0, 0]]
    >>> find_leading_coefficient_row(matrix, [0], 1)
    1
    >>> matrix = [[0, 0, 2], [0, 10, 0], [1, 0, 0]]
    >>> find_leading_coefficient_row(matrix, [], 2)
    0
    >>> matrix = [[1, 0, 2], [0, 10, 0], [0, 0, 3]]
    >>> find_leading_coefficient_row(matrix, [0], 2)
    2
    >>> matrix = [[1, 0, 2], [0, 1, 5], [0, 0, 0], [0, 0, 3]]
    >>> find_leading_coefficient_row(matrix, [0, 1], 2)
    3
    """

    index = -1
    row = 0
    while index == -1 and row < len(matrix):
        if row not in placed_rows and matrix[row][column] != 0:
            index = row
        row +=1
    return index


def elimination (matrix: list[list[float]]) -> None:
    """Given a matrix, run the elimination algorithm on it and reduce it to
    row-reduced echelon form.

    Preconditions: matrix is in proper format (ie equal rows, equal columns)


    """

    COLUMNS = len(matrix[0])
    ROWS = len(matrix)
    placed_rows = []

    # iterate through columns
    # print(matrix[0])
    row = 0
    
    # iterate until the matrix "hits a wall", be it the bottom or the right
    while row < COLUMNS and row < ROWS:
        # find row with non-zero coefficient
        row_with_leading_coefficient = find_leading_coefficient_row(matrix, placed_rows, row)

        # if there's a non-zero coefficient, switch rows with the current one
        if row_with_leading_coefficient != -1:
            # print('rows to switch: ', row, ' and ', row_with_leading_coefficient)
            switch_row(matrix, row, row_with_leading_coefficient)

            # turn non-zero coefficient into leading one
            leading_coefficient = matrix[row][row]
            scale_row(matrix[row], 1/leading_coefficient)

            # clear column
            for clear_row in range(ROWS):
                if clear_row != row:
                    wrong_coefficient = matrix[clear_row][row]
                    if wrong_coefficient != 0.0:
                        scale_and_add_row(matrix[row], matrix[clear_row], -wrong_coefficient)

            # signify that this row has a leading one
            placed_rows.append(row)
            
        # advance to next row
        row += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()