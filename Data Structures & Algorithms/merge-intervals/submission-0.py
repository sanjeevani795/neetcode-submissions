class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x : x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = merged[-1][1]
            if prev_end >= start:
                merged[-1][1] = max(prev_end, end)
            else:
                merged.append([start, end])

        return merged