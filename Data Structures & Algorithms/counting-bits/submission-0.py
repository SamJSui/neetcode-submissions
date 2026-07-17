class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0]
        for i in range(1, n+1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            counts.append(count)
        return counts