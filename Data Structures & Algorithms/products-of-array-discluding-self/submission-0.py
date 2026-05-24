class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        premutl = 1
        postmutl = 1
        for i in range(len(nums)):
            pre.append(premutl)
            premutl *= nums[i]

        for j in range(len(nums)-1,-1,-1):
            post.append(postmutl)
            postmutl *= nums[j]
        
        for k in range(len(nums)):
            pre[k] *= post[len(nums)-k-1]

        return pre

        