class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        minPrice = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            #if price < minPrice:
            #    minPrice = price
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
            if price < minPrice:
                minPrice = price

        return maxProfit