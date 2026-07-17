class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = Counter(nums)
        elements = [(-v, k) for k, v in track.items()]
        heapq.heapify(elements)
        ret = []
        for i in range(k):
            cnt, val = heapq.heappop(elements)
            ret.append(val)
        return ret