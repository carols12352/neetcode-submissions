class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_prof = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            max_prof = max(max_prof, prices[right] - prices[left])
            right += 1
        return max_prof