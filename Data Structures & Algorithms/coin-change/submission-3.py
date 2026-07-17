class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def dfs(i: int, target: int):
            if target == 0:
                return 0
            elif i >= n or target < 0:
                return float('inf')
            print(coins[i], target)
            
            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = min(
                dfs(i, target-coins[i])+1, # Stay, add same coin
                dfs(i+1, target), # Skip
            )
            return memo[(i, target)]
        
        ret = dfs(0, amount)
        return ret if ret != float('inf') else -1