# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        def dfs(node):
            nonlocal maxi
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maxi = max(maxi, left+right)
            return 1+max(left, right)
        dfs(root)
        return maxi

            