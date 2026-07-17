class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * n
        def dfs(i: int):
            if i > n:
                return 0
            elif i == n:
                return 1
            if memo[i] != 0:
                return memo[i]

            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]
        return dfs(0)