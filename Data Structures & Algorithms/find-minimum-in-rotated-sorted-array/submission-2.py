class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (r+l)//2
            print(nums[m], nums[r])
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
        return nums[l]