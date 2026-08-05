class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in lookup and lookup[(target - nums[i])] != i:
                return [i, lookup[(target - nums[i])]]

        