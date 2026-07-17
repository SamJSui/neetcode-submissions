class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0
        l, r = 0, 0
        n = len(s)
        while r < n:
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1
            longest = max(longest, len(window))
        return longest