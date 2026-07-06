class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def sort_key(interval):
            return (interval[0], -interval[1])
        intervals.sort(key=sort_key)
        remaining=0
        max_right=0
        for start, end in intervals:
            if end>max_right:
                remaining+=1
                max_right= end
        return remaining