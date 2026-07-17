# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        def dfs(node: TreeNode):
            if not node:
                return
            if len(nums) >= k:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        dfs(root)
        return nums[k-1]