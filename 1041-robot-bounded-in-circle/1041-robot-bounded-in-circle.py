class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        - Keep the coordinates of the starting point
        - Do the sequence and see if you end up at the initial coordinates
        - Case G, Case L and Case R
        '''
        
        start = [0,0]
        direction = (0,1)
        
        for s in instructions:
            if s == 'G':
                start[0] += direction[0]
                start[1] += direction[1]
            elif s == 'L':
                direction = (-direction[1], direction[0])
            elif s == 'R':
                direction = (direction[1], -direction[0])
                
        return start == [0,0] or direction != (0,1)