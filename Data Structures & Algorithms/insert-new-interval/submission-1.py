class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        new_intervals = []
        prev_start, prev_end = intervals[0]
        for start, end in intervals[1:]:
            if start <= prev_end:
                prev_end = max(prev_end, end)
            else:
                new_intervals.append([prev_start, prev_end])
                prev_start, prev_end = start, end
        new_intervals.append([prev_start, prev_end])
        return new_intervals