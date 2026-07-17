class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigits(num: int) -> int:
            summ = 0
            while num != 0:
                summ += (num % 10)**2
                num //= 10
            return summ

        slow = n
        fast = sumDigits(n)
        print(f"slow {slow} fast {fast}")

        while slow != fast:
            fast = sumDigits(fast)
            fast = sumDigits(fast)
            slow = sumDigits(slow)
        return fast == 1