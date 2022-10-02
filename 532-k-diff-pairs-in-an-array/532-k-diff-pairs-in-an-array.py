class Solution:
    #time - O(n)
    #space - O(n)
    def findPairs(self, nums: List[int], k: int) -> int:
        dict = {}
        count = 0
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
        
        for key, val in dict.items():
            value = key - k
            if k == 0:
                count = count + 1 if val > 1 else count
            elif value in dict:
                count += 1
                
        return count