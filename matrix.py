class MatrixSolver:
    """
    This is the MatrixSolver class, it contains different types of algorithems
    that allow you to walk the matrix in different orders.
    Currently implemented:
        - spiral order (outside to inside)
        - horizontal (zigzag)
    """
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def solve_spiral(self) -> list[int]:
        """
        traversing a matrix from outside to the inside
        """
        left = 0
        top = 0
        right = len(self.matrix[0])
        bottom = len(self.matrix)
        result = []
        if not self._is_matrix_valid():
            return result
        
        while left < right and top < bottom:
            # walk from upper left to upper right corner
            result += self._walk_horizontal(top, left, right)
            top += 1

            # walk from upper right to lower right corner
            result += self._walk_vertical(right-1, top, bottom)
            right -= 1

            if not (left < right and top < bottom):
                break

            # walk from lower right to lower left corner
            # subtract 1 from 'bottom' -> list out of index
            result += self._walk_horizontal(bottom-1, right, left)
            bottom -= 1

            # walk from lower left to upper left corner
            result += self._walk_vertical(left, bottom, top)
            left += 1

        return result

    def solve_horizontal(self) -> list[int]:
        """
        traversing a matrix horizontally from left to right and back
        """
        left = 0
        top = 0
        right = len(self.matrix[0])
        bottom = len(self.matrix)
        result = []
        if not self._is_matrix_valid():
            return result
    
        while top < bottom:
            # walk from left to right
            result += self._walk_horizontal(top, left, right)
            top += 1

            if not top < bottom:
                break

            # walk from right to left
            result += self._walk_horizontal(top, right, left)
            top += 1
        
        return result

    def _is_matrix_valid(self):
        """
        Check if the Matrix provided is a 'valid' matrix.
        This is not a complete check since row and column 1 to x 
        could stil contain more than N amount of entries (practically)
        """
        if len(self.matrix[0]) != len(self.matrix):
            return False
        return True

    def _walk_horizontal(self, row: int, start: int, end:int) -> list[int]:
        """
        fuction takes in a row number, starting point and end point
        and will return a list of numbers. Walking backwards is handled
        within the function
        """
        if start > end:
            # walk from left to right, but revert the outcome
            return self.matrix[row][end:start][::-1]
        # walk from left to right
        return self.matrix[row][start:end] 

    def _walk_vertical(self, column: int, start: int, end: int) -> list[int]:
        """
        fuction takes in a column number, starting point and end point
        and will return a list of numbers. Walking upwards is handled
        within the function
        """
        result = []
        if start > end:
            # walk from  to start but revert the outcome
            for i in range(end, start):
                result.append(self.matrix[i][column])
            return result[::-1]
        else:
            # walk from bottom to top
            for i in range(start, end):
                result.append(self.matrix[i][column])
            return result

