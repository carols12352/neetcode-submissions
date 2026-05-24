class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic =  {}
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i],0) + 1

        return len(dic) != len(nums)