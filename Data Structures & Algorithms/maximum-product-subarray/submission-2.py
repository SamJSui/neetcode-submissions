class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        maxi = mini = 1
        for num in nums:
            maxi, mini = max(num, maxi*num, mini*num), min(num, mini*num, maxi*num)
            max_product = max(max_product, maxi)
        return max_product