# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, maxi: int):
            if not root:
                return 0
            cur = 0 if root.val < maxi else 1
            
            left = dfs(root.left, max(maxi,root.val))
            right = dfs(root.right, max(maxi,root.val))

            return left + right + cur
        return dfs(root, root.val)
        

            
            
        