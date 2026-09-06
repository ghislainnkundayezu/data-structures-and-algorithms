class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]

        if n <= 1:
            result = 1
        else:
            result = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)

        memo[n] = result
        return result