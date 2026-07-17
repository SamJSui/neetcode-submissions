class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        while l <= r:
            candidate = numbers[l] + numbers[r]
            if candidate == target:
                return [l+1, r+1]
            
            if candidate > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]