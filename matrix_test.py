from matrix import MatrixSolver
from fixtures import matrix_ex1, matrix_ex2, matrix_invalid_row, matrix_invalid_column


class TestMatrixClass:
    def setup(self):
        self.mx_small = MatrixSolver(matrix_ex1)
        self.mx_big = MatrixSolver(matrix_ex2)
        self.mx_invalid_row = MatrixSolver(matrix_invalid_row)
        self.mx_invalid_column = MatrixSolver(matrix_invalid_column)

    def tes_matrix_invalid_row(self):
        assert self.mx_invalid_row._is_matrix_valid() == False
        assert self.mx_invalid_row.solve_horizontal() == []
        assert self.mx_invalid_row.solve_spiral() == []

    def test_matrix_invalid_column(self):
        assert self.mx_invalid_column._is_matrix_valid() == False
        assert self.mx_invalid_column.solve_horizontal() == []
        assert self.mx_invalid_column.solve_spiral() == []

    def test_walk_horizontal(self):
        assert self.mx_small._walk_horizontal(0, 0, 4) == [1, 2, 3, 4] 
        assert self.mx_small._walk_horizontal(3, 1, 3) == [14, 15] 
        assert self.mx_small._walk_horizontal(1, 4, 1) == [8, 7, 6] 
        assert self.mx_small._walk_horizontal(2, 2, 0) == [10, 9] 

    def test_walk_vertically(self):
        assert self.mx_small._walk_vertical(0, 1, 3) == [5, 9]
        assert self.mx_small._walk_vertical(2, 4, 0) == [15, 11, 7, 3]
    
    def test_matrix_valid_small(self):
        assert self.mx_small._is_matrix_valid() == True
        assert self.mx_small.solve_horizontal() == [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 16, 15, 14, 13]
        assert self.mx_small.solve_spiral() == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    def test_matrix_valid_big(self):
        assert self.mx_big._is_matrix_valid() == True
        assert self.mx_big.solve_horizontal() == [1, 2, 3, 4, 5, 6, 12, 11, 10, 9, 8, 7, 13, 14, 15, 16, 17, 18, 24, 23, 22, 21, 20, 19, 25, 26, 27, 28, 29, 30, 36, 35, 34, 33, 32, 31]
        assert self.mx_big.solve_spiral() == [1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 35, 34, 33, 32, 31, 25, 19, 13, 7, 8, 9, 10, 11, 17, 23, 29, 28, 27, 26, 20, 14, 15, 16, 22, 21]
