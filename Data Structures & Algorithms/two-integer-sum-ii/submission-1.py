class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            summ = numbers[l]+numbers[r]
            print(summ)
            if summ == target: return [l+1, r+1]
            if summ > target:
                r -= 1
            else:
                l += 1
        return [0, 1]