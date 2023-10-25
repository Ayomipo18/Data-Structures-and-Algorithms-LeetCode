class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        - get the freq of the words, use an hashmap
        - put those words into a priorityqueue, we want to use the min priorityqueue
        - so if len of pq > k, remove from pq
        - then our pq will have lowest to highest arranged
        - we then remove from our pq, put it in our result arr and then reverse it.
        
        - n = len(words)
        - time - O(nlogk)
        - space - O(n) -> from hashmap
        '''
        
        words_map = {}
        words_heap = []
        result = []
        
        #O(n)
        for word in words:
            if word not in words_map:
                words_map[word] = 0
            words_map[word] += 1
            
        #O(nlogk)
        for key in words_map:
            node = Node(key, words_map[key])
            heapq.heappush(words_heap, node)
            if len(words_heap) > k:
                heapq.heappop(words_heap)
            
        #O(klogk)
        while words_heap:
            val = heapq.heappop(words_heap)
            result.append(val.word)
            
        #O(k)
        result.reverse()
        return result
        
        
            
        