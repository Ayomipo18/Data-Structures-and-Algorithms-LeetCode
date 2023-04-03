class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        people = []
        each boat carries at most 2 people with a set limit
        can carry 2 people at the same time provided the sum of weight of those 2 people is at most limit
        return min number of boats to carry every given person.
        [3,5,3,4]
        -put 3 in one group, check can any other number fit into this group? no, no number can
        -put 5 in another group, limit, yes
        -put 3 in another group. any other number? no
        -put 4, yes, no other number
        
        [3,2,3,4]
        -put 3 in one group, any other number? yes
        
        [3,1,2,5,4] -> [5,4,3,2,1] -> [(5), (4,1), (3,2)]
        sort it first
        
        [5,4,4,3]
        priority queue or normal queue??
        
        [1,1,1,1] limit = 1
        
        we can use greedy, two pointers, put one at the beginning of the array and one at the ending of the array
        since i always need to pair both highest and lowest, just move the pointers when you resolve both
        '''
        left, right = 0, len(people) - 1
        people.sort()
        boats = 0
    
        while left <= right:
            rem = limit - people[right]
            right -= 1
            boats += 1
            if left <= right and rem >= people[left]:
                left += 1
        
        return boats
        