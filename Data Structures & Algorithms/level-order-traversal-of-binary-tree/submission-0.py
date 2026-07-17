# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ret = []
        while q and q[0]:
            level = []
            n = len(q)
            for _ in range(n):
                top = q.pop()
                if top.left:
                    q.appendleft(top.left)
                if top.right:
                    q.appendleft(top.right)
                level.append(top.val)
            ret.append(level)
        return ret