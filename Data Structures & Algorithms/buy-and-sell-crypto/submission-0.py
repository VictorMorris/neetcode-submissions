class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for i in range(len(prices)):
            buy = min(prices[i], buy)
            maxProfit = max(maxProfit, prices[i]-buy)

        return maxProfit