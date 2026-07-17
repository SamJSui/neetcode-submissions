class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def dfs(i, total):
            if i >= n: return total
            return min(dfs(i+1, total+cost[i]), dfs(i+2, total+cost[i]))
        return min(dfs(0, 0), dfs(1, 0))