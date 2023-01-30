class Solution:
    def tribonacci(self, n: int) -> int:
        sequence = [0, 1, 1]
        if n < 3:
            return sequence[n]
        return self.n_tribonacci(n, sequence)
    
    def n_tribonacci(self, n, sequence):
        if len(sequence) > n:
            return sequence[n]
        result = self.n_tribonacci(n-3, sequence) + self.n_tribonacci(n-2, sequence) + self.n_tribonacci(n-1, sequence)
        sequence.append(result)
        return result