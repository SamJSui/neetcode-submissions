class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        tmp = []
        print(self.nums)
        for _ in range(self.k):
            tmp.append(heapq.heappop(self.nums))
        print(tmp, '\n')
        for val in tmp:
            heapq.heappush(self.nums, val)
        return -tmp[-1]
