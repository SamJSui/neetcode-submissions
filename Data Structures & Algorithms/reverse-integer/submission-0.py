class Solution:
    def reverse(self, x: int) -> int:
        MAX_VALUE = 2**31-1
        digits = 0
        ret = 0
        tmp = abs(x)
        while tmp:
            digits += 1
            tmp //= 10
        tmp = abs(x)
        while digits:
            ret += abs(tmp % 10) * 10**digits
            print(ret)
            digits -= 1
            tmp //= 10
        if x < 0: return -(ret // 10)
        elif ret > MAX_VALUE or ret < -MAX_VALUE: return 0
        else: return ret // 10
