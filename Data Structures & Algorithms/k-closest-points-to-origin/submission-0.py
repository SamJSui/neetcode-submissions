class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap, ret = [], []
        for x, y in points:
            heapq.heappush(minheap, [math.sqrt(x**2+y**2), x, y])
        while k:
            dist, x, y = heapq.heappop(minheap)
            ret.append([x, y])
            k -= 1
        return ret