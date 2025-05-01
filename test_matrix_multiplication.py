# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 11:18:35 2025

@author: chank
"""

import unittest

from matrix_multiplication import multiply

class TestMultiply (unittest.TestCase):
    """Tests the multiply function."""
    
    def setUp(self):
        self.non_square_example1 = [[1.0, 2.0, 3.0], 
                                    [5.0, 4.0, 6.0]]
        self.non_square_example2 = [[2.0, 3.0, 4.0, 6.0],
                                    [2.0, 6.0, 9.0, 0.0],
                                    [1.0, 3.0, 7.0, 2.0]]
        
        self.square_example1 = [[1.0, 2.0], 
                               [5.0, 4.0]]
        self.square_example2 = [[2.0, 6.0],
                                [1.0, 3.0]]
        
        self.identity = [[1.0, 0.0, 0.0],
                         [0.0, 1.0, 0.0],
                         [0.0, 0.0, 1.0]]
        self.identity_example_1 = [[3.0, 4.0, 1.0],
                                   [4.0, 5.0, 2.0],
                                   [6.0, 7.0, 8.0],
                                   [6.0, 5.0, 8.0]]
        self.identity_example_2 = [[3.0, 4.0],
                                   [4.0, 5.0],
                                   [6.0, 7.0]]
        
    def test_non_square (self):
        """Tests the case of multiplying two non-square matrices."""
        actual = multiply(self.non_square_example1, self.non_square_example2)
        expected = [[9.0, 24.0, 43.0, 12.0],
                    [24.0, 57.0, 98.0, 42.0]]
        self.assertEqual(actual, expected, 'hey!')
        
    def test_square (self):
        """Tests the case of multiplying two square matrices, makes sure it's not commutative."""
        actual_1 = multiply(self.square_example1, self.square_example2)
        expected_1 = [[4.0, 12.0],
                      [14.0, 42.0]]
        self.assertEqual(actual_1, expected_1, 'hey!')
        
        actual_2 = multiply(self.square_example2, self.square_example1)
        expected_2 = [[32.0, 28.0],
                      [16.0, 14.0]]
        self.assertEqual(actual_2, expected_2, 'hey!')
        
    def test_identity (self):
        """Tests how multiply works with identity matrices."""
        actual_1 = multiply(self.identity_example_1, self.identity)
        expected_1 = self.identity_example_1
        self.assertEqual(actual_1, expected_1, 'hey!')
        
        actual_2 = multiply(self.identity, self.identity_example_2)
        expected_2 = self.identity_example_2
        self.assertEqual(actual_2, expected_2, 'hey!')
    
        
if __name__ == '__main__':
    unittest.main(exit=False)