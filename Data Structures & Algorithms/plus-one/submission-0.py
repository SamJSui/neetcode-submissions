class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = deque()
        n = len(digits)
        carry = 1
        
        for i in range(n-1, -1, -1):
            res = (digits[i]+carry)
            ret.appendleft(res % 10)
            carry = res // 10
        if carry:
            ret.appendleft(carry)

        return ret
