class Solution:
    #time - O(nlogn)
    #space - O(1)
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        hardest_worker = logs[0][0]
        longest_time = logs[0][1]
        
        for i in range(1, len(logs)):
            log = logs[i]
            log_time = log[1] - logs[i-1][1]
            if log_time > longest_time:
                hardest_worker = log[0]
                longest_time = log_time
            elif log_time == longest_time and hardest_worker > log[0]:
                hardest_worker = log[0]
        
        return hardest_worker