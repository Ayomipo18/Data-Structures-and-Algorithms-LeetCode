class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        - O(n*n)
        '''
        result = [[1]]
        if numRows < 2:
            return result
        
        for i in range(1, numRows):
            arr = [1]
            for j in range(0, i-1):
                arr.append(result[i-1][j] + result[i-1][j+1])
            arr.append(1)
            result.append(arr)
            
        return result