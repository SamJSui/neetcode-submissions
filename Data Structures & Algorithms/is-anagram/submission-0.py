class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        db1, db2 = Counter(s), Counter(t)
        return db1 == db2