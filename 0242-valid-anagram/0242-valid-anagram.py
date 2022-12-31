class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for val in s:
            if not val in map:
                map[val] = 0
            map[val] += 1

        for val in t:
            if not val in map:
                return False
            map[val] -= 1
            if map[val] < 0:
                return False

        return True 