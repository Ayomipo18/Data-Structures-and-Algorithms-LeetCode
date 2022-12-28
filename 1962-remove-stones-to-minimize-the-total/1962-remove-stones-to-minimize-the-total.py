class Solution:
    '''
    n = length of piles
    time - O(n + klogn)
    space - O(n)
    '''
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        while k > 0:
            k -= 1
            pile = -heapq.heappop(heap)
            pile = math.ceil(pile / 2)
            heapq.heappush(heap, -pile)

        return -sum(heap)