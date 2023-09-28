class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        - we will use a monotonic increasing stack
        - we keep track of the frequency of characters initially
        - we also keep track of letters we have put in the stack.
        - So intially fill up all the frequencies of the characters
        - then go thru s,
            - if s[i] has been put into the stac(if it is in seen)k, no need to put it again(continue)
            - while stack and s[i] < stack.top and freq[stack.top] > 0:
                - remove the stack.top
                - set see[stack.top] = F
            - add s[i] to stack
            - remobe freq of s[i]
            
        - do stack.join and then reverse it
        - example of bcab
        - the sta
        '''
        
        stack = []
        freq = [0] * 26
        seen = [False] * 26
        
        for val in s:
            freq[ord(val) - 97] += 1
            
        for val in s:
            valCode = ord(val) - 97
            if seen[valCode]:
                freq[valCode] -= 1
                continue
            while stack and val < stack[-1] and freq[ord(stack[-1]) - 97] > 0:
                seen[ord(stack[-1]) - 97] = False
                stack.pop()
                
            stack.append(val)
            freq[valCode] -= 1
            seen[valCode] = True
            
            
        return "".join(stack)