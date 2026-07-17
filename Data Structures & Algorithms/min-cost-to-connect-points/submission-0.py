class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        cost = 0

        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        minheap = [node for node in adj[0]]
        heapq.heapify(minheap)
        visited = set([0])
        while len(visited) < n:
            dist, top = heapq.heappop(minheap)
            while top in visited:
                dist, top = heapq.heappop(minheap)
            visited.add(top)
            cost += dist
            
            for node in adj[top]:
                heapq.heappush(minheap, node)

        return cost

        