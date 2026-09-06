class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = 0

        for i in range(1, len(prices)):
            if prices[start] >= prices[i]:
                start=i
                continue
            else:
                profit = prices[i] - prices[start]
                max_profit = max(max_profit, profit)

        return max_profit