class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        overlap = 0
        print(intervals)
        start, end = intervals[0]
        for s, e in intervals[1:]:
            print(start, end, s, e)
            if s < end:
                overlap += 1
                end = min(e, end)
            else:
                start, end = s, e
        return overlap