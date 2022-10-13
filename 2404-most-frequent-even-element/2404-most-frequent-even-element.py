class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        map = {}
        
        for i, value in enumerate(nums):
            if value % 2 == 0:
                if value not in map:
                    map[value] = 0
                map[value] += 1
        
        freq = -1
        answer = -1
        dict = sorted(map.items(), key=lambda x:x[0])
        
        print(dict)
        print(map)
        for value in dict:
            curr_freq = value[1]
            if curr_freq > freq:
                freq = curr_freq
                answer = value[0]
                
        return answer