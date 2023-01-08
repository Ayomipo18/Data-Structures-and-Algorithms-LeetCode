class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        result = []
        dict = defaultdict(int)
        
        for i in items1:
            dict[i[0]] += i[1]
        for i in items2:
            dict[i[0]] += i[1]
            
        for key, value in dict.items():
            result.append([key, value])
        
        result.sort()
        
        return result