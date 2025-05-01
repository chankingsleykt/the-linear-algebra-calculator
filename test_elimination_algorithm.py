import unittest
from copy import deepcopy

from elimination_algorithm import elimination as elmn

class TestElimination(unittest.TestCase):
    """Test the elimination function."""

    def setUp (self):
        self.zero_example = [[0.0, 0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0, 0.0]]

        self.independent_example =  [[0.0, 0.0, 1.0],
                                     [1.0, 5.0, 3.0],
                                     [7.0, 1.0, 1.0]]

        self.dependent_example =  [[1.0, 0.0, 1.0],
                                   [1.0, 5.0, 3.0],
                                   [1.0, 0.0, 1.0]]

        self.onebyone_example = [[5.0]]

        self.onerow_example = [[1232.0, 1232.0, 1232.0, 123213.0]]

        self.onecolumn_example = [[0.0],
                                  [1232.0],
                                  [1232.0],
                                  [123213.0]]
        
        self.more_columns_than_rows_example = [[0.0, 4.0],
                                               [1232.0, 2.0],
                                               [1232.0, 1.0],
                                               [123213.0, 5.0]]
        
        self.more_rows_than_columns_example = [[0.0, 4.0, 1232.0, 2.0],
                                               [1232.0, 1.0, 123213.0, 5.0]]

        self.rref_out_of_order_example = [[0.0, 0.0, 1.0, 0.0],
                                          [0.0, 1.0, 0.0, 0.0],
                                          [0.0, 0.0, 0.0, 1.0],
                                          [1.0, 0.0, 0.0, 0.0]]

        self.damiano_example = [[4.0, 2.0, -1.0, 1.0, -1.0],
                                [1.0, 1.0, 0.0, 2.0, 2.0],
                                [6.0, 4.0, -1.0, 5.0, 3.0]]


    def test_zero_matrix (self):
        """Test elimination with the zero matrix."""
        actual = deepcopy(self.zero_example)
        elmn(actual)
        expected = [[0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0]]
        self.assertEqual(actual, expected, 'hey!')


    def test_independent_matrix (self):
        """Test elimination with an independent matrix."""
        actual = deepcopy(self.independent_example)
        elmn(actual)
        expected = [[1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0]]
        self.assertEqual(actual, expected, 'hey!')


    def test_dependent_matrix (self):
        """Test elimination with a dependent matrix."""
        actual = deepcopy(self.dependent_example)
        elmn(actual)
        expected = [[1.0, 0.0, 1.0],
                    [0.0, 1.0, 0.4],
                    [0.0, 0.0, 0.0]]
        self.assertEqual(actual, expected, 'hey!')


    def test_onebyone_matrix (self):
        """Test elimination with a one-by-one matrix."""
        actual = deepcopy(self.onebyone_example)
        elmn(actual)
        expected = [[1.0]]
        self.assertEqual(actual, expected, 'hey!')


    def test_onerow_matrix (self):
        """Test elimination with a one-row matrix."""
        actual = deepcopy(self.onerow_example)
        elmn(actual)
        expected = [[1.0, 1.0, 1.0, 100.01055194805195]]
        self.assertEqual(actual, expected, 'hey!')


    def test_onecolumn_matrix (self):
        """Test elimination with a one-column matrix."""
        actual = deepcopy(self.onecolumn_example)
        elmn(actual)
        expected = [[1.0],
                    [0.0],
                    [0.0],
                    [0.0]]
        self.assertEqual(actual, expected, 'hey!')
        
    def test_more_columns_than_rows_matrix (self):
        """Test elimination with a matrix that has more columns than rows."""
        actual = deepcopy(self.more_columns_than_rows_example)
        elmn(actual)
        expected = [[1.0, 0.0], 
                    [0.0, 0.9999999999999999], 
                    [0.0, 0.0], 
                    [0.0, 0.0]]
        self.assertEqual(actual, expected, 'hey!')
        
    def test_more_rows_than_columns_matrix (self):
        """Test elimination with a matrix that has more rows than columns."""
        actual = deepcopy(self.more_rows_than_columns_example)
        elmn(actual)
        expected = [[1.0, 0.0, 99.76055194805195, 0.003652597402597403], 
                    [0.0, 1.0, 308.0, 0.5]]
        self.assertEqual(actual, expected, 'hey!')

    def test_rref_out_of_order_matrix (self):
        """Test elimination with a matrix in RREF, but the rows are out of order."""
        actual = deepcopy(self.rref_out_of_order_example)
        elmn(actual)
        expected = [[1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0]]
        self.assertEqual(actual, expected, 'hey!')


    def test_damiano_matrix (self):
        """Test elimination with a matrix in Damiano and Little's textbook."""
        actual = deepcopy(self.damiano_example)
        elmn(actual)
        expected = [[1.0, 0.0, -0.5, -1.5, -2.5],
                    [0.0, 1.0, 0.5, 3.5, 4.5],
                    [0.0, 0.0, 0.0, 0.0, 0.0]]
        self.assertEqual(actual, expected, 'hey!')

if __name__ == '__main__':
    unittest.main(exit=False)