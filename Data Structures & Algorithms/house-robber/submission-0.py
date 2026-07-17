class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0]*n
        def dfs(i: int):
            if i >= n:
                return 0
            if memo[i] != 0:
                return memo[i]
            memo[i] = max(dfs(i+1), nums[i]+dfs(i+2))
            return memo[i]
        return dfs(0)