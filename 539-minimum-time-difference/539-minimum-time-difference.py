class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, time in enumerate(timePoints):
            hrs, minutes = time.split(":")
            minutes_past_midnight = int(hrs) * 60 + int(minutes)
            timePoints[i] = minutes_past_midnight
        
        timePoints.sort()
        res = 1440 + timePoints[0] - timePoints[-1]
        
        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i] - timePoints[i-1])

        
        return res
    
#we want to convert each time to mintues
#sort it to compute(difference) two time close to each other, and that's what will give lowest time
#compute(difference) the first and last value in the array and 
#then compare each value close to each other and get min with result