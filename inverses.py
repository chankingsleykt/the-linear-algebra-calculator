# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 11:21:21 2025

@author: chank
"""

from elimination_algorithm import elimination
from copy import deepcopy

def is_identity(matrix: list[list[float]]) -> bool:
    """
    Parameters
    ----------
    matrix : list[list[float]]
        A matrix.

    Returns
    -------
    bool
        whether or not the matrix is an identity matrix.

    >>> is_identity([[1.0, 0.0, 0.0],
    ...              [0.0, 1.0, 0.0],
    ...              [0.0, 0.0, 1.0]])
    True
    >>> is_identity([[1.0, 3.0, 0.0],
    ...              [0.0, 1.0, 0.0],
    ...              [4.5, 6.3, 1.0]])
    False
    >>> is_identity([[1.0, 0.0, 0.0],
    ...              [0.0, 2.0, 0.0],
    ...              [0.0, .00, 1.0]])
    False
    >>> is_identity([[1.0, 0.0, 0.0],
    ...              [0.0, 1.0, 0.0]])
    False
    """
    
    ROWS = len(matrix)
    COLUMNS = len(matrix[0])
    if ROWS != COLUMNS:
        return False

    for row in range(ROWS):
        for column in range(COLUMNS):
            if column == row:
                if matrix[row][column] != 1.0:
                    return False
            else:
                if matrix[row][column] != 0.0:
                    return False
        
    return True


def invert (matrix: list[list[float]]) -> list[list[float]]:
    """
    Parameters
    ----------
    matrix : list[list[float]]
        A matrix to be inverted.

    Returns
    -------
    The inverted matrix, or [] if the matrix cannot be inverted.

    """
    
    ROWS = len(matrix)
    COLUMNS = len(matrix[0])
    
    new_matrix = deepcopy(matrix)
    
    # Create an identity row of the right size to add onto matrix
    for i in range(ROWS):
        identity_row = []
        for j in range(COLUMNS):
            if j == i:
                identity_row.append(1.0)
            else:
                identity_row.append(0.0)
        new_matrix[i].extend(identity_row)
        
    elimination(new_matrix)
    
    # Split the matrix into the original and the inverted to see if the original's become the identity
    og_matrix = []
    inverted_matrix = []
    for i in range(ROWS):
        og_matrix.append(new_matrix[i][0:COLUMNS])
        inverted_matrix.append(new_matrix[i][COLUMNS:])
    
    if is_identity(og_matrix):
        return inverted_matrix
    return []

    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()