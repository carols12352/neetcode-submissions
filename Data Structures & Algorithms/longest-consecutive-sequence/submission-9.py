class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        max_length = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                cur = 0
                while x + cur in nums_set:
                    length += 1
                    cur += 1
                max_length = max(max_length,length)
                length = 0
                cur = 0
        return max_length
