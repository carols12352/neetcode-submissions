class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_set = set(numbers)
        res = []
        for nums in nums_set:
            if target - nums in nums_set and target-nums != nums:
                res = [numbers.index(nums) + 1, numbers.index(target-nums) + 1]

        return sorted(res)