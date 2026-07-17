class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = [False] * (len(nums)+1)
        for num in nums:
            d[num] = True
        print(d)
        for num in range(len(nums)+1):
            print(num, d[num])
            if not d[num]:
                return num
        return 0