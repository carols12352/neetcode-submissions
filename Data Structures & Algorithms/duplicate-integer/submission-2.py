class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for i in nums:
            if cnt[i] != 1:
                return True

        return False