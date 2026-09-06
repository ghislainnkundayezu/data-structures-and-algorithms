class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        el_size = len(matrix[0])
        size = len(matrix) * el_size
        l, r = 0, size - 1
         
        while r >= l:
            mid = (r + l) // 2
            mid_val = matrix[mid // el_size][mid % el_size]
            if (mid_val) < target:
                l = mid + 1
            elif (mid_val) > target:
                r = mid - 1
            else:
                return True

        return False