class SegmentTree:
    def __init__(self, n):
        n = (2 * n) + 1
        height = math.ceil(math.log2(n))
        size = (2 * (2**height)) - 1
        self.st_arr = [0] * size
    
    def query(self, index, s_left, s_right, min_val, target):
        if target >= s_right:
            return self.st_arr[index]
        elif target < s_left or min_val > s_right:
            return 0
        else:
            mid = s_left + (s_right - s_left) //2
            return self.query(2*index+1, s_left, mid, min_val, target) + self.query(2*index+2, mid+1, s_right, min_val, target)
    
    def update(self, index, s_left, s_right, target):
        if s_left > target or s_right < target:
            return
        
        self.st_arr[index] += 1
        
        if s_left != s_right:
            mid = s_left + (s_right - s_left) // 2
            self.update(2*index+1, s_left, mid, target)
            self.update(2*index+2, mid+1, s_right, target)
            
# class BIT:
#     def __init__(self, n):
#         size = n + 1
#         self.bit_arr = [0] * size
        
#     def query(self, index):
#         result = 0
        
#         while index > 0:
#             result += self.bit_arr[index]
#             index -= (-index & index)
            
#         return result
        
#     def update(self, index):
#         while index < len(self.bit_arr):
#             self.bit_arr[index] += 1
#             index += (-index & index)
    
class Solution:
    '''
    - create the segment tree
        - the top node contains the sum of all elements in the array
        - then we partition by finding mid = l + (r-l//2)
        - then do a recursive call for 0, mid, index = 2*i+1 = 2*0+1
        - recursive call for mid, len(arr)-1
        - if l == r, just return nums[l]
        - do nums[index] = left + right recursive call
    '''
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        st, n, offset = SegmentTree(10**4), len(nums), 10**4
        min_val = min(nums)
        result = [0] * n
        
        for i in range(n-1, -1, -1):
            result[i] = st.query(0, 0, 2 * offset, min_val + offset, nums[i]+offset-1)
            st.update(0, 0, 2 * offset, nums[i]+offset)
        
        return result
    
    '''
    - Binary Index Tree
        -BIT
        - create the BIT
        - start from the end of input array
        - for each num in nums, do a query(from node+1 up till parent)
        - then do update, do a getnext(from node+1 while node+1 in range)
        - perform range sum query of buckets [-inf, n-1], where n is current number
        - because we want n - 1 for range sum query of [-inf, n-1], not n, subtract 1 from i
    '''
    
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         bt, n, offset = BIT((2*10**4)+1), len(nums), 10**4
#         result = [0] * n
        
#         for i in range(n-1, -1, -1):
#             result[i] = bt.query(nums[i]+offset)
#             bt.update(nums[i]+1+offset)
            
#         return result