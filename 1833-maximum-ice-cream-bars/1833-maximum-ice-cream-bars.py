class Solution:
    '''
    - sort the costs array [1,1,2,3,4]
    - for each cost in costs.
    - if coins >= cost, coins -= cost
    - increase count if the above operation is possible
    - else return count
    - return count at the end
    - time complexity - O(nlogn)
    - space complexity - O(n) because of sorting
    '''
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                return count
        return count