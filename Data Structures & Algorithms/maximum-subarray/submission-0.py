class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = 0
        for num in nums:
            curr += num
            maxi = max(maxi, curr)
            curr = max(curr, 0)
        return maxi