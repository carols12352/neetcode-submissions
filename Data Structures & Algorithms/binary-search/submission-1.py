class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.binia(nums,left,right,target)
    
    def binia(self,nums:List[int], left, right, target) ->int:
        if left > right:
            return -1
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binia(nums, 0, mid - 1, target)
        else:
            return self.binia(nums, mid + 1, right, target)

