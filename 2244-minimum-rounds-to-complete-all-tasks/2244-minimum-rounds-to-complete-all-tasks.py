class Solution:
    '''
    time - O(n)
    space - O(n)
    where n is the length of tasks
    '''
    def minimumRounds(self, tasks: List[int]) -> int:
        dict = {}
        rounds = 0
        
        for task in tasks:
            if task not in dict:
                dict[task] = 0
            dict[task] += 1
        
        for key,val in dict.items():
            if val == 1:
                return -1
            if val % 3 == 0:
                rounds += (val // 3)
            elif val % 3 == 1:
                rounds += ((val - 4) // 3) + 2
            elif val % 3 == 2:
                rounds += (val // 3) + 1
        return rounds
        