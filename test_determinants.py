# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 18:20:58 2025

@author: chank
"""

import unittest

from determinants import det
from inverses import invert


class TestDet(unittest.TestCase):
    """Tests the det function."""
    def setUp(self):
        self.one_by_one_example = [[9.0]]
        
        self.two_by_two_example = [[9.0, 6.0],
                                   [4.0, 3.2]]
        
        self.generic_example = [[5.0, 3.0, 5.0, 4.0, 1.0],
                                [2.0, 4.0, 6.0, 7.0, 8.0],
                                [6.0, 9.0, 1.0, 24.0, 6.0],
                                [7.0, 1.0, 12.0, 12.0, 5.0],
                                [9.0, 8.0, 4.0, 2.0, 3.0]]
        
        self.dependent_example = [[0.0, 3.0, 4.0],
                                  [0.0, 1.0, 0.0],
                                  [0.0, 0.0, 1.0]]
        
        self.identity_example = [[1.0, 0.0, 0.0, 0.0],
                                 [0.0, 1.0, 0.0, 0.0],
                                 [0.0, 0.0, 1.0, 0.0],
                                 [0.0, 0.0, 0.0, 1.0]]
        
        self.alternating_example_1 = [[1.0, 2.0, 3.0, 4.0],
                                      [0.0, 1.0, 67.0, 5.0],
                                      [3.0, -12.0, 1.0, 3.0],
                                      [7.0, 8.0, 9.0, 1.0]]
        
        self.alternating_example_2 = [[1.0, 2.0, 3.0, 4.0],
                                      [0.0, 1.0, 67.0, 5.0],
                                      [-3.0, 12.0, -1.0, -3.0],
                                      [7.0, 8.0, 9.0, 1.0]]
        
        self.multilinear_example_1 = [[1.0, 2.0, 3.0, 4.0],
                                      [0.0, 1.0, 67.0, 5.0],
                                      [3.0, -12.0, 1.0, 3.0],
                                      [7.0, 8.0, 9.0, 1.0]]
        
        self.multilinear_example_2 = [[1.0, 2.0, 3.0, 4.0],
                                      [0.0, 2.0, 134.0, 10.0],
                                      [3.0, -12.0, 1.0, 3.0],
                                      [7.0, 8.0, 9.0, 1.0]]
        
        self.inverse_example = [[1.0, 2.0, 3.0, 4.0],
                                [0.0, 2.0, 13.0, 10.0],
                                [3.0, -12.0, 1.0, 3.0],
                                [7.0, 8.0, 9.0, 1.0]]
   
        
    def test_one_by_one (self):
        """Test the case of a one-by-one matrix"""
        actual = det(self.one_by_one_example)
        expected = 9.0
        self.assertEqual(actual, expected, 'hey!')
      
        
    def test_two_by_two (self):
        """Test the case of a two-by-two matrix"""
        actual = det(self.two_by_two_example)
        expected = 4.800000000000001
        self.assertEqual(actual, expected, 'hey!')  
        
        
    def test_generic (self):
        """Test the case of a generic square matrix"""
        actual = det(self.generic_example)
        expected = -17130.0
        self.assertEqual(actual, expected, 'hey!')  
        
    
    def test_dependent (self):
        """Test the case of a square matrix that has linearly independent rows."""
        actual = det(self.dependent_example)
        expected = 0.0
        self.assertEqual(actual, expected, 'hey!')
        
        
    def test_identity (self):
        """Test the case of the identity matrix."""
        actual = det(self.identity_example)
        expected = 1.0
        self.assertEqual(actual, expected, 'hey!')
    
    
    def test_alternating (self):
        """Test if det is alternating."""
        actual = det(self.alternating_example_1)
        expected = -det(self.alternating_example_2)
        self.assertEqual(actual, expected, 'hey!')
        
        
    def test_multilinear (self):
        """Test if det is multilinear."""
        actual = det(self.multilinear_example_2)
        expected = 2*det(self.alternating_example_1)
        self.assertEqual(actual, expected, 'hey!')
        
    
    def test_inverse (self):
        """Test if the det of an invertible matrix is the reciprocal of the det of its inverse."""
        actual = det(invert(self.inverse_example))
        expected = 1/det(self.inverse_example)
        self.assertEqual(actual, expected, 'hey!')

        
if __name__ == '__main__':
    unittest.main(exit=False)