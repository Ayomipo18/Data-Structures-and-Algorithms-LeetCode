class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        new_intervals = sorted(intervals, key=lambda x:x[0])
        result.append(new_intervals[0])
        
        for i in range(1, len(new_intervals)):
            interval = new_intervals[i]
            if result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
                
        return result