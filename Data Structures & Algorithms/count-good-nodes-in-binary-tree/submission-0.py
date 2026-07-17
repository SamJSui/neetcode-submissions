# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxi):
            if not node: return 0
            left = dfs(node.left, max(maxi, node.val))
            right = dfs(node.right, max(maxi, node.val))
            return left+right if node.val < maxi else left+right+1
        return dfs(root, -101)