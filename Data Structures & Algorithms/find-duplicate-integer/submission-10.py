class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            print(f'slow: {slow} -> {nums[slow]}')
            print(f'fast: {fast} -> {nums[fast]} -> {nums[nums[fast]]}')
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        print(f'slow: {slow}, fast: {fast}')
        start = 0
        while True:
            print(f'slow: {slow} -> {nums[slow]}')
            print(f'start: {start} -> {nums[start]}')
            slow = nums[slow]
            start = nums[start]
            if slow == start:
                return slow