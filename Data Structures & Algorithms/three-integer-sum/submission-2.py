class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        n = len(nums)
        for i, val in enumerate(nums):
            if val > 0:
                break
            l, r = i + 1, n-1
            if i > 0 and val == nums[i-1]:
                continue
            
            while l < r:
                summ = val + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    triplets.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return triplets