class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        n = len(nums)
        nums.sort()
        for i, val in enumerate(nums):
            if val > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            l, r = i+1, n-1
            while l < r:
                summ = val+nums[l]+nums[r]
                if summ == 0:
                    triplets.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                if summ < 0:
                    l += 1
                
                if summ > 0:
                    r -= 1
        return triplets