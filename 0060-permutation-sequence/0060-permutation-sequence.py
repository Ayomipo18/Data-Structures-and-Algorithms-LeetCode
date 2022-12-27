class Solution:
    '''
    time - O(n^2)
    space - O(n)
    '''
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            factorials.append(i * factorials[i-1])
            nums.append(str(i+1))
        
        k -= 1
        output = []
        
        for i in range(n-1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            output.append(str(nums[idx]))
            del nums[idx]
            
        return "".join(output)