class Solution:
    #time - O(2^n)
    #space - O(n)
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.result = []
        for i in range(1, 10):
            self.backtrack(i, n-1, k)

        return self.result

    def backtrack(self, value, n, k):
        if n == 0:
            self.result.append(value)
            return
        
        last_val = value % 10
        num = value * 10

        if last_val + k <= 9:
            self.backtrack(num + last_val + k, n - 1, k)
        
        if last_val - k >= 0 and k > 0:
            self.backtrack(num + last_val - k, n - 1, k)

'''
[181, 292, 707, 818, 929]
1 -> 1 + 7 = 8 -> 8 - 7 = 1
2 -> 9 -> 2
7 -> 0 -> 7
8 -> 1 -> 8
9 -> 2 -> 9
if num + k not valid, do num - k

n = 2, k = 1
[12, 10, 23, 21, 34, 32]
1 -> 2
1 -> 0
2 -> 3
2 -> 1
3 -> 4
3 -> 2
'''