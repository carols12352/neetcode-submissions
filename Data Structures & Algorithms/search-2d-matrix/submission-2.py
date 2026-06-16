class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                return self.binia(matrix[i],0,len(matrix[i]) - 1,target)
        return False


    def binia(self,nums:List[int], left, right, target) -> bool:
        if left > right:
            return False
        mid = (left + right)//2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return self.binia(nums, left, mid - 1, target)
        else:
            return self.binia(nums, mid + 1, right, target)