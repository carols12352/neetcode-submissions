class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        sort_arr = sorted(nums)
        length = 1
        cur_length = 1
        for i in range(len(nums) - 1):
            length = max(cur_length, length)
            if sort_arr[i] + 1 == sort_arr[i+1]:
                cur_length += 1
            elif sort_arr[i] == sort_arr[i+1]:
                continue
            else:
                cur_length = 1
        return max(cur_length, length)
