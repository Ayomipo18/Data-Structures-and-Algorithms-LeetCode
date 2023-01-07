class Solution:
    '''
    - go through the gas array, when we find a value gas - cost which is < 0, we set that total_tank to 0 and move to the next start position
    - also check that total gas can cover total cost(total_gas >= total_cost)
    - it's a greedy question
    - time - O(n)
    - space - O(1)
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        total_tank = 0
    
        for i in range(len(gas)):
            cur_tank = gas[i] - cost[i]
            total_tank += cur_tank
            if total_tank < 0:
                total_tank = 0
                start = i + 1
        return start