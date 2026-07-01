# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        count = 0

        def travers(root):
            nonlocal ans, count
            if not root:
                return
            travers(root.left)
            count += 1
            if count == k:
                ans = root.val
                return
            travers(root.right)
        travers(root)
        return ans