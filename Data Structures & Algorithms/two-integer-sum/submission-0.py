class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        db = {}
        for i, num in enumerate(nums):
            # print(db.get(target-num))
            if db.get(target-num, -1) >= 0:
                return [db[target-num], i]
            db[num] = i
            # print(db)
        return [-1, -1]