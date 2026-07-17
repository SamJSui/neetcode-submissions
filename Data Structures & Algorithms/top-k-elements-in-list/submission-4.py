class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = Counter(nums) # O(n)
        elements = [(-v, k) for k, v in track.items()] # O(n)
        heapq.heapify(elements) # O(n)
        ret = []
        for i in range(k): # O(k)
            cnt, val = heapq.heappop(elements)
            ret.append(val)
        return ret