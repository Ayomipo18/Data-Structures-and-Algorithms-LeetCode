class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.split(" ")
        count = 0
        
        for word in new_s:
            if word == "":
                continue
            count = len(word)
        
        return count