class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [g-c for g, c in zip(gas, cost)]
        n = len(gas)
        def dfs(i, total):
            for j in range(i+1, n+i+1):
                total += diff[j%n]
                if total < 0: return False
            return True

        for i in range(n):
            if diff[i] >= 0 and dfs(i, diff[i]):
                return i

        return -1