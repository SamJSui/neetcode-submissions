class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        db = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            db[sorted_s] = db.get(sorted_s, []) + [s]
        return list(db.values())