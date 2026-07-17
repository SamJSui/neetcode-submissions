class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, summ):
            if i == len(nums):
                return 1 if summ == target else 0
            return dfs(i+1, summ+nums[i]) + dfs(i+1, summ-nums[i])
        return dfs(0, 0)