class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        even and odd expansion basically
        - function to do palindrom check
        '''
        left = 0
        maxLength = 0
        
        for i in range(len(s)):
            maxEvenLength = self.isPalindrome(i, i, s)
            maxOddLength = self.isPalindrome(i, i+1, s)
            maxTempLength = max(maxEvenLength, maxOddLength)
            if maxTempLength > maxLength:
                left = i - ((maxTempLength - 1) // 2)
                maxLength = maxTempLength
                
        return s[left: left+maxLength]
        
            
    def isPalindrome(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1