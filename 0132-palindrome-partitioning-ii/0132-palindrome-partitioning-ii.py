class Solution:
    '''
    where n is the length of s
    time - O(n^2)
    space - O(n)
    '''
    def minCut(self, s: str) -> int:
        n = len(s)
        memocuts = [0] * n

        for i in range(1, n):
            memocuts[i] = i
        
        for i in range(n):
            self.is_palindrome(i,i,s,memocuts)
            self.is_palindrome(i,i+1,s,memocuts)

        return memocuts[n-1]

    def is_palindrome(self, start, end, s, memocuts):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            new_cut = 0 if start == 0 else memocuts[start - 1] + 1
            memocuts[end] = min(memocuts[end], new_cut)
            start -= 1
            end += 1