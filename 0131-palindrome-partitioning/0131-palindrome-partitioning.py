class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #n = len(s)
        #time - O(n * 2^n)
        #space - O(n)
        result = []
        self.check_partition(s, 0, result, [])
        return result
    
    def check_partition(self, s, index, result, curr_result):
        if index >= len(s):
            result.append(curr_result.copy()) #O(len(s))
            return
        
        for i in range(index, len(s)):
            if self.is_palindrome(s, index, i):
                curr_result.append(s[index:i+1])
                self.check_partition(s, i+1, result, curr_result)
                curr_result.pop()
        
        return
        
    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
#recursive function
#do for loop in our recursive fun, if our curret string is a palindrome, run the recurisve function on it