class Solution:
    '''
    time - O(n)
    space - O(n)
    where n is the length of nums
    - so we want to keep the max num value for k initially,
    - then for subsequent k positions, if our current max num is still valid(within k range), we take it as our max at the moment
    - also, as we move, i want to be kepping the next max value i can get.
    - if i see a new max, i just want to put it in its place of max values,
    - meaning, if i see a new value, i should determine if it's the biggest max or in between max
    [7] -> [3, 3, 5, 5, 7]. l = 0 -> 1
    [4,5]
    [0,1] = [1]
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, output = collections.deque(), []
        l = r = 0
        
        while r < len(nums):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if r+1 >= k:
                output.append(nums[q[0]])
                l += 1
                
            r += 1
        
        return output