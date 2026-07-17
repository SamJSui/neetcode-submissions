class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for c in num1:
            n1 += int(c)
            n1 *= 10
        n1 //= 10
        for c in num2:
            n2 += int(c)
            n2 *= 10
        n2 //= 10
        return str(n1*n2)
