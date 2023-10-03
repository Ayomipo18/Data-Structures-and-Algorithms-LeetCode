class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for c in s:
            n = ord(c)
            ans += chr(n+32) if n > 64 and n < 91 else c
        return ans