class Solution:
    def trap(self, height: List[int]) -> int:
        high_l = 0
        l = 0
        r = len(height) - 1
        high_r = 0
        total = 0
        while l < r:
            high_r = max(high_r,height[r])
            high_l = max(high_l, height[l])
            if high_l > high_r:
                total += min(high_r,high_l) - height[r]
                r -= 1
            else:
                total += min(high_r,high_l) - height[l]
                l += 1


        return total