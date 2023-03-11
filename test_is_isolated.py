import unittest
import numpy as np
from main import is_isolated
from main import fill_diagonal

class TestIsIsolated(unittest.TestCase):
    
    def setUp(self):
        self.matrix = np.array([
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [1, 0, 0, 0, 0],
          [0, 0, 0, 1, 0]])

    def test_valid_matrix_1(self):
        diagonals = np.array([
          [0,1,3,4],
          [0,3,3,0]])
        matrix = fill_diagonal(self.matrix.copy(), diagonals)    
        self.assertTrue(is_isolated(matrix))

    def test_invalid_matrix_1(self):
        diagonals = np.array([
          [0,0,2,2]])
        matrix = fill_diagonal(self.matrix.copy(), diagonals)   
        self.assertFalse(is_isolated(matrix))
    
    def test_invalid_matrix_2(self):
        diagonals = np.array([
          [0,1,3,2],
          [3,0,0,3],
          [0,0,3,3]])
        matrix = fill_diagonal(self.matrix.copy(), diagonals) 
        self.assertFalse(is_isolated(matrix))

    def test_valid_matrix_2(self):
        diagonals = np.array([
          [1,0,3,2],
          [3,0,0,3],
          [3,2,1,4]])
        matrix = fill_diagonal(self.matrix.copy(), diagonals)          
        self.assertTrue(is_isolated(matrix))    

if __name__ == '__main__':
    unittest.main()