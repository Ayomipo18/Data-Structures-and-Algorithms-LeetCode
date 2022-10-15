class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

            time = [x % 60 for x in time]
            count = Counter(time)
            out = 0 

            for value in range(1,30):

                if count[value] > 0 and count[60-value] > 0:
                    out = out + (count[value]*count[60-value])

            if count[30] >= 2:
                out = out + ((count[30])*(count[30]-1))//2

            if count[0] >= 2:
                out = out + ((count[0])*(count[0]-1))//2


            return out
        