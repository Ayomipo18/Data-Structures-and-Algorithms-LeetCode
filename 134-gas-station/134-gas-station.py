class Solution:
    #time - O(n)
    #space - O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        starting_position = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                curr_tank = 0
                starting_position = i + 1
                
        return starting_position if total_tank >= 0 else -1
#have three variables one for total_tank, one for curr_tank(which gets reset to 0), then starting_position
#loop through has array
    #calculate total_tank = gas[i] - cost[i]
    #same thing for curr_tank
    #so we check if curr_tank < 0:
        #set starting_position = i + 1
        #curr_tank = 0
#return total_tank >= 0: starting_position : -1