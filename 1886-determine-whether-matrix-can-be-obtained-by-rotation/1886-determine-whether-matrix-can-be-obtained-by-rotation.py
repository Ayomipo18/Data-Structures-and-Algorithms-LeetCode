class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        '''
        rotate matrix and compare with target
        Time - O(n^2)
        Space - O(1)
        '''
        def rotate_matrix(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            for i in range(n):
                matrix[i].reverse()

        for _ in range(4):
            if mat == target:
                return True
            rotate_matrix(mat)

        return False