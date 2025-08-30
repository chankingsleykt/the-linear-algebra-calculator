import unittest

import inner_products

class TestStandard_ip(unittest.TestCase):
    """Test the standard inner product function."""

    def setUp(self):
        self.basic_example = [[5.7, 4], [3, 2.1]]
        self.negatives = [[-8, -4, 3], [7, -6.8, 1]]
        self.orthogonal = [[6, 7], [7, -6]]


    def test_basic (self):
        """Tests the basic example."""
        actual = inner_products.standard_ip(self.basic_example[0], self.basic_example[1])
        expected = 25.5
        self.assertEqual(actual, expected, 'hey!')
    
    def test_negatives (self):
        """Tests the negatives example."""
        actual = inner_products.standard_ip(self.negatives[0], self.negatives[1])
        expected = -25.8
        self.assertEqual(actual, expected, 'hey!')

    def test_orthogonal (self):
        """Tests the orthogonal example."""
        actual = inner_products.standard_ip(self.orthogonal[0], self.orthogonal[1])
        expected = 0.0
        self.assertEqual(actual, expected, 'hey!')


class TestProjection(unittest.TestCase):
    """Test the projection function."""


if __name__ == '__main__':
    unittest.main(exit=False)
    print(inner_products.standard_ip([0, 1], [0, 1]))
    print(inner_products.standard_ip([5.0, 6.0, 7.0], [5.0, 6.0, 7.0]))