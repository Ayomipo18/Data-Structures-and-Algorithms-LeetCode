class Solution:
    def __init__(self):
        self.count = 0
        self.memo = {}

    def countSubstrings(self, s: str) -> int:
        self.backtrack(s, 0, len(s)-1)
        return self.count

    def backtrack(self, s, start, end):
        key = str(start) + "-" + str(end)

        if key in self.memo:
            return self.memo[key]

        if start > end:
            return 1
        
        if s[start] == s[end]:
            self.memo[key] = self.backtrack(s, start + 1, end - 1)
        else:
            self.memo[key] = 0
        
        self.backtrack(s, start, end - 1)
        self.backtrack(s, start + 1, end)
        
        self.count += self.memo[key]

        return self.memo[key]