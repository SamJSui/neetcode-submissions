class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        db = Counter(nums)
        return any(val > 1 for val in db.values())