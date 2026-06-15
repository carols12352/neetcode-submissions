class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left <= right:
            cur_area = (right - left)*min(heights[right],heights[left])
            max_area = max(max_area, cur_area)
            # if max_area < (right - left - 1)*min(heights[right],heights[left + 1]):
            #     left += 1
            # elif max_area < (right - 1 - left )*min(heights[right - 1],heights[left]):
            #     right -= 1
            # else:
            #     left += 1
            #     right -=1
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area