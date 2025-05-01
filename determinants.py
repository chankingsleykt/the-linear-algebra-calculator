# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:42:36 2025

@author: chank
"""

def minor(matrix:list[list[float]], i:int, j:int) -> list[list[float]]:
    """

    Parameters
    ----------
    matrix : list[list[float]]
        The matrix to generate the ij-minor from.
    i : int
        row i.
    j : int
        column j.

    Returns
    -------
    list[list[float]]
        the ij-minor of matrix.
        
    >>> minor([[1.0, 0.0, 0.0], [2.0, 4.0, 5.0], [0.0, 0.0, 0.0]], 1, 0)
    [[0.0, 0.0], [0.0, 0.0]]
    >>> minor([[1.0, 0.0, -0.5, -1.5, -2.5], [0.0, 1.0, 0.5, 3.5, 4.5], [0.0, 0.0, 0.0, 0.0, 0.0]], 1, 2)
    [[1.0, 0.0, -1.5, -2.5], [0.0, 0.0, 0.0, 0.0]]
    """
    
    result = []
    for row in matrix[0:i]:
        new_row = row[0:j]
        new_row.extend(row[j+1:])
        result.append(new_row)
        
    for row in matrix[i+1:]:
        new_row = row[0:j]
        new_row.extend(row[j+1:])
        result.append(new_row)
    return result


def det(matrix: list[list[float]]) -> float:
    """
    Given a matrix, return its determinant.
    
    Pre-condition: the matrix is square, that is, the rows = columns.
    """
    ROWS = len(matrix)
    COLUMNS = len(matrix[0])
    
    if ROWS == COLUMNS == 1:
        return matrix[0][0]
    
    result = 0
    for column_num in range(COLUMNS):
        result += ((-1)**(column_num+1+1))*matrix[0][column_num]*det(minor(matrix, 0, column_num))
    return result
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()