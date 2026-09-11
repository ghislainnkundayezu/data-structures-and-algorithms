class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestProfit = 0
        l = 0
        
        for i in range(1, len(prices)):
            currentProfit = prices[i] - prices[l]
            if currentProfit < 0:
                l = i
            else:
                highestProfit = max(highestProfit, currentProfit)

        return highestProfit
