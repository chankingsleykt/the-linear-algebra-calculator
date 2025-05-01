# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 15:10:44 2025

@author: chank
"""

import unittest

import inverses

class TestInvert(unittest.TestCase):
    """Test the invert function."""
    
    def setUp(self):
        self.identity_example = [[1.0, 0.0, 0.0],
                                 [0.0, 1.0, 0.0],
                                 [0.0, 0.0, 1.0]]
        
        self.invertible_example = [[2.0, 1.0, 0.0, -3.0],
                                   [0.0, 1.0, 4.0, 2.0],
                                   [1.0, 0.0, 2.0, 5.0],
                                   [2.0, -2.0, 1.0, 1.0]]
        
        self.non_invertible_square_example = [[1.0, 2.0, 3.0, 4.0],
                                              [2.0, 4.0, 6.0, 8.0],
                                              [5.0, 6.0, 7.0, 8.0],
                                              [0.0, 0.0, 0.0, 0.0]]
        
        self.more_rows_than_columns_example = [[2.0, 1.0, 1.0],
                                               [3.0, 2.0, 1.0]]
        
        self.more_columns_than_rows_example = [[2.0, 1.0, 1.0],
                                               [3.0, 2.0, 1.0],
                                               [0.0, 2.0, 1.0],
                                               [3.0, 3.0, 1.0]]
        
        
    def test_identity(self):
        """Tests the identity case."""
        actual = inverses.invert(self.identity_example)
        expected = [[1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0]]
        self.assertEqual(actual, expected, 'hey!')
        
        
    def test_invertible(self):
        """Tests the case of an invertible matrix."""
        actual = inverses.invert(self.invertible_example)
        expected = [[0.30434782608695654, -0.13043478260869565, 0.2173913043478261, 0.08695652173913043],
                    [0.2608695652173913, -0.026086956521739202, 0.24347826086956514, -0.3826086956521739],
                    [-0.0434782608695652, 0.30434782608695654, -0.17391304347826086, 0.13043478260869565],
                    [-0.04347826086956522, -0.09565217391304348, 0.22608695652173913, -0.06956521739130435]]
        self.assertEqual(actual, expected, 'hey!')
        
        
    def test_non_invertible_square(self):
        """Tests the case of a non-invertible square matrix."""
        actual = inverses.invert(self.non_invertible_square_example)
        self.maxDiff = None
        expected =[]
        self.assertEqual(actual, expected, 'hey!')
    
    
    def test_more_rows_than_columns(self):
        """Tests the case of a matrix with more rows than columns."""
        actual = inverses.invert(self.more_rows_than_columns_example)
        expected = []
        self.assertEqual(actual, expected , 'hey!')
        
        
    def test_more_columns_than_rows(self):
        """Tests the case of a matrix with more columns than rows."""
        actual = inverses.invert(self.more_columns_than_rows_example)
        expected = []
        self.assertEqual(actual, expected , 'hey!')
        
        
        
if __name__ == '__main__':
    unittest.main(exit=False)