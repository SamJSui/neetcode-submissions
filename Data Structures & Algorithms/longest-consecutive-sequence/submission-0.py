class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        visited = set()
        for num in nums:
            seq = 1
            while num-1 in nums:
                seq += 1
                visited.add(num)
                num -= 1
            longest = max(longest, seq)
        return longest