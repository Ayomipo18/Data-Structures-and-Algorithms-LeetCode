class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        [-6,2,7,11,13,20] t = 9
        - if last two combinations are higher than target, move rigtmost val
        - if combination less than target, move leftmostt
        - if combination == target, return the indexes + 1
        '''
        
        lIndex = 0
        rIndex = len(numbers) - 1
        
        while lIndex < rIndex:
            val = numbers[lIndex] + numbers[rIndex]
            if val > target:
                rIndex -= 1
            elif val < target:
                lIndex += 1
            else:
                return [lIndex+1, rIndex+1]
        
        return []