class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        radius = 0
        i = 0
        left, right = None, None
        
        for index, house in enumerate(houses):
            while (i < len(heaters) - 1 and heaters[i] <= house):
                i += 1
            
            left = abs(house - (heaters[i - 1] if i > 0 else heaters[0]))
            right = abs(heaters[i] - house)
            
            radius = max(radius, min(left, right))
            
        return radius

'''
[1, 2, 3] [2]
radius = 0
i = 0
left = none
right = none

house = 1 -> 2 -> 3
left = 1 -> 0 -> 1
right = 1 -> 0 -> 1
radius = 1 -> 1

[1, 2, 3, 4, 5] [1, 1, 3, 4]
radius = 0
i = 0 -> 2
left = none
right = none

house = 1 -> 2
left = 0 -> 
right = 2 -> 
radius = 0 -> 
'''