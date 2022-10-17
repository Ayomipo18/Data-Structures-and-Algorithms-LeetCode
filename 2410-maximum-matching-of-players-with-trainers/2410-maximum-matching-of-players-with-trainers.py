class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        players_index, trainers_index  = 0, 0
        
        while players_index < len(players) and trainers_index < len(trainers):
            if players[players_index] <= trainers[trainers_index]:
                players_index += 1
                trainers_index += 1
                count += 1
            else:
                trainers_index += 1
                
        return count