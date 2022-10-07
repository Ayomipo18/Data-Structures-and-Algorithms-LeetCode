class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        result = ""
        
        for i, val in enumerate(words):
            left, right = 0, len(val) - 1
            det = 0
            
            while left <= right:
                if val[left] != val[right]:
                    det = 0
                    break
                left += 1
                right -= 1
                det += 1
            
            if det > 0 and len(result) == 0:
                result = val
            
        return result