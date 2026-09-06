class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            result = 1
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
    
        return result