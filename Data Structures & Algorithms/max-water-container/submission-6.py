class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tot_max = 0
        l,r = 0, len(heights) - 1
        while l < r:
            tot_max = max(tot_max, min(heights[l],heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return tot_max