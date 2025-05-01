# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 20:07:12 2025

@author: chank
"""

def multiply(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    """

    Parameters
    ----------
    matrix1 : list[list[float]]
        the first mxn matrix.
    matrix2 : list[list[float]]
        the second nxk matrix.

    Returns
    -------
    list[list[float]]
        an mxk matrix,the product of matrix1 and matrix2.
        
    Preconditions: matrix1 and matrix2 must be able to be multiplied, that is,
    matrix1 is mxn and matrix2 is nxk.

    """
    
    result = []
    
    ROWS_1 = len(matrix1)
    COLUMNS_1 = len(matrix1[0])
    COLUMNS_2 = len(matrix2[0])
    
    for row_1 in range (ROWS_1):
        row = []
        for column_2 in range (COLUMNS_2):
            entry = 0
            for column_1 in range (COLUMNS_1):
                entry += matrix1[row_1][column_1]*matrix2[column_1][column_2]
            row.append(entry)
        result.append(row)
            
    
        
    return result