class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for x in count.values():
            if x != 1:
                return True
        return False