class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        sta = []

        for i, h in enumerate(heights):
            start = i
            while sta and sta[-1][1] > h:
                idx, height = sta.pop()
                max_area = max(max_area, (i - idx) * height)

                start = idx
            sta.append([start, h])
        
        for i, h in sta:
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area





