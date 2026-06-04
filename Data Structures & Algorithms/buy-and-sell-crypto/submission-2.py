class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxprofit = 0
        for r in range(1, len(prices)):
            current = prices[r] - prices[l]
            if current > maxprofit:
                maxprofit = current
            while prices[l] > prices[r]:
                l += 1
        return maxprofit
