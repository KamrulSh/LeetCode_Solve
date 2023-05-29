class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float("inf")
        maxProfit = 0
        for i, price in enumerate(prices):
            if prices[i] < minValue:
                minValue = prices[i]
            else:
                maxProfit = max(prices[i] - minValue, maxProfit)
        return maxProfit