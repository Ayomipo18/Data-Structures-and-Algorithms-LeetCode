class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        from queue import Queue
        bank = set(bank)
        queue = Queue()
        
        queue.put((start, 0))
        seen = {start}
        
        while queue.qsize() > 0:
            node, steps = queue.get()
            
            if node == end:
                return steps
            
            for char in "ACGT":
                for i in range(len(node)):
                    neighbour = node[:i] + char + node[i+1:]
                    if neighbour not in seen and neighbour in bank:
                        queue.put((neighbour, steps + 1))
                        seen.add(neighbour)
        return -1
                