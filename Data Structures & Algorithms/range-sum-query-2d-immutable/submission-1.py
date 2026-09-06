class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        #self.prefix_matrix = [row[:] for row in self.matrix]

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                u = self.matrix[r-1][c] if r > 0 else 0
                l = self.matrix[r][c-1] if c > 0 else 0 
                a = self.matrix[r-1][c-1] if ((r > 0) and (c > 0)) else 0

                self.matrix[r][c] += (u + l - a) 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a1 = self.matrix[row2][col2]
        a2 = self.matrix[row1-1][col2] if row1>0 else 0
        a3 = self.matrix[row2][col1-1] if (col1>0) else 0
        a4 = self.matrix[row1-1][col1-1] if (row1>0and col1>0) else 0

        total_area = a1 - a2 - (a3 - a4)
        return total_area      


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)