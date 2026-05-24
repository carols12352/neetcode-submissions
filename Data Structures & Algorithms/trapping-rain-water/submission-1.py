class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        postfix = []
        for i in range(len(height) + 1):
            maxleft = 0
            maxright = 0
            for j in range(0, i):
                maxleft = max(maxleft,height[j])
            for k in range(i + 1,len(height)):
                maxright = max(maxright, height[k])
            prefix.append(maxleft)
            postfix.append(maxright)

        totcount = 0
        for j in range(len(height) - 1):
            if min(prefix[j], postfix[j]) - height[j] >= 0:
                totcount += min(prefix[j], postfix[j]) - height[j]

        return totcount
            

            

        
                

        
            