class Solution:
    '''
    whee n is the length of ratings
    time - O(n)
    space - O(n)
    '''
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1] * n

        for i in range(n):
            if i-1 >= 0 and ratings[i] > ratings[i-1]:
                result[i] = max(result[i], result[i-1] + 1)

        for i in range(n-1, -1, -1):
            if i+1 < n and ratings[i] > ratings[i+1]:
                result[i] = max(result[i], result[i+1] + 1)

        return sum(result)