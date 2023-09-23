# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         '''
#         - Keep the coordinates of the starting point
#         - Do the sequence and see if you end up at the initial coordinates
#         - Case G, Case L and Case R
#         '''
        
#         x, y = 0, 0
#         direction = 0
#         turned = False
        
#         for s in instructions:
#             if s == 'G':
#                 if direction == 0 or direction == 2:
#                     y += 1
#                 elif direction == 1 or direction == 3:
#                     x += 1
#             elif s == 'L':
#                 direction -= 1
#                 if direction < 0:
#                     direction = 3
#                 turned = True
#             elif s == 'R':
#                 direction += 1
#                 if direction > 3:
#                     direction = 0
#                 turned = True
                
#             print("x",x)
#             print("y",y)
#             print("dir", direction)
#         return True if (x == 0 or y == 0) and (turned == True) else False

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0,1)
        start = [0,0]
        
        for x in instructions:
            if x == 'G':
                start[0] += direction[0]
                start[1] += direction[1]
            elif x == 'L':
                direction = (-direction[1], direction[0])
            elif x == 'R':
                direction = (direction[1], -direction[0])
        
        return start == [0,0] or direction != (0,1)