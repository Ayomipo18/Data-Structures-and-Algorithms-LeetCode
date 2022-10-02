class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        from queue import PriorityQueue
        pq = PriorityQueue()
        
        for i in range(len(names)):
            pq.put(((-1 * heights[i]), names[i]))
        
        index = 0
        while not pq.empty():
            height, name = pq.get()
            names[index] = name
            index += 1
            
        return names