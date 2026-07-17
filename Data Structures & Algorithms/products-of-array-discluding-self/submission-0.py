class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prefix = [1]
        for num in nums[:-1]:
            prod *= num
            prefix.append(prod)
        postfix = [1]
        prod = 1
        for num in nums[:0:-1]:
            prod *= num
            postfix.append(prod)
        return [pre*post for pre, post in zip(prefix, postfix[::-1])]