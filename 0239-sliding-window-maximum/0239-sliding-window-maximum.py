class Solution:
    '''
    time - O(n)
    space - O(n)
    where n is the length of nums array
    - so initially, when taking k window, example 1, we would go through k and find the max value
    - we notice that when doing the next k window, we touch some elements again. how can we reduce this repititon
    - E.g for [1,3,-1] -> [3,-1,-3], we touch 3, and -1 again, how can we reduce this repetition
    - we can do that by not touching 3 and -1 again, just jump to -3
    - so when i jump to -3, do i want to still compare with the prev k values?, noo
    - since i know that my max is 3 and it's still within range of k atm, i will just use 3
    - so a stack/queue can help me cos it will keep all values until a particular condition is reached.
    - i want to always keep values in my data structure in decreasing order, with the max always at the front of my ds and next max value after it
    - do i want to keep all values? not all but some, stack will be too expensive to remove all the values from it
    [3,-1,-3] -> [7]
    - while r <= len(nums)
        - while l < r:
            - while ds and nums[ds[-1]] < curr_val, remove ds[-1]
                - pop from array
            - append curr_elem index to array [6]
            - l+=1 -> 4 -> 5 -> 6 -> 7
        -append(ds[0]) to output [3,3, 5, 5, 6]
        - r = l + 1 -> 5 -> 6 -> 7 -> 8
    - while r < len(nums)
        - while ds and nums[ds[-1]] < curr_val, remove ds[-1]
            - pop from array
        - append curr_elem index to array [6]
        - if ds[0] < l, pop the value from the ds
        - if r + 1 >= k, append ds[0]
            - l+=1
        - r += 1
        -append(ds[0]) to output [3,3, 5, 5, 6]
        - r = l + 1 -> 5 -> 6 -> 7 -> 8
    '''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q, output = deque(), []
        l = r = 0
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if q[0] < l:
                q.popleft()
            
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
            
        return output