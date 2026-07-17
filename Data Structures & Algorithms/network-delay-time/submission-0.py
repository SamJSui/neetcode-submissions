class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ret = 0

        adj = {i: [] for i in range(1, n+1)}
        for s, d, t in times:
            adj[s].append((d, t))

        minheap = [(0, k)]
        visited = set()

        while minheap:
            w1, s1 = heapq.heappop(minheap)
            if s1 in visited: continue
            visited.add(s1)
            ret = w1
            for dst, t in adj[s1]:
                if dst in visited: continue
                heapq.heappush(minheap, (w1 + t, dst))

        return ret if len(visited) == n else -1

