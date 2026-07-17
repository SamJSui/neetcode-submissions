class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        def solve(sub_nums):
            prev2, prev1 = 0, 0
            for num in sub_nums:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1

        return max(solve(nums[:-1]), solve(nums[1:]))