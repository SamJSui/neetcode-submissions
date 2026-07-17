class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, ret = len(gas), 0
        if sum(gas) < sum(cost): return -1

        diff = [g-c for g, c in zip(gas, cost)]
        total = 0

        for i in range(n):
            total += diff[i]
            if total < 0:
                ret = i+1
                total = 0

        return ret