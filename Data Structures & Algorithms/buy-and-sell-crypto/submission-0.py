class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        left = 0
        right = 1
        while right <= len(prices) - 1:
            if prices[right] - prices[left] > prof:
                prof = prices[right] - prices[left]
            elif prices[right] - prices[left] <= 0:
                left = right
            right += 1
        return prof