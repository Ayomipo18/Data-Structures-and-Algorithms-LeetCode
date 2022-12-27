class Solution:
    '''
    n - len(capacity)
    time - O(nlogn)
    space - O(n) because of sorting
    '''
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count = 0
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        
        capacity.sort()

        for val in capacity:
            additionalRocks -= val
            if additionalRocks < 0:
                return count
            else:
                count += 1

        return count