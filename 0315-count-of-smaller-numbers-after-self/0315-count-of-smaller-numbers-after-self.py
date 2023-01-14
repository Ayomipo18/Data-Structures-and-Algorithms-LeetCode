class SegmentTree:
    def __init__(self, nums):
        n = (2 * 10**4) + 1
        height = math.ceil(math.log2(n))
        size = (2 * (2**height)) - 1
        self.st_arr = [0] * size
        min_val, max_val = min(nums), max(nums)
        #self.construct(nums, 0, min_val, max_val)
        
    def construct(self, nums, index, left, right):
        if left == right:
            self.st_arr[index] = nums[left]
            return nums[left]
        
        mid = left + (right-left)//2
        self.st_arr[index] = self.construct(nums, 2*index+1, left, mid) + self.construct(nums, 2*index+2, mid+1, right)
        return self.st_arr[index]
    
    def query(self, index, s_left, s_right, target):
        if s_left == target and s_right == target:
            return 0
        if target > s_right:
            return self.st_arr[index]
        elif target < s_left:
            return 0
        else:
            mid = s_left + (s_right - s_left) //2
            return self.query(2*index+1, s_left, mid, target) + self.query(2*index+2, mid+1, s_right, target)
    
    def update(self, index, s_left, s_right, target):
        if s_left > target or s_right < target:
            return
        
        self.st_arr[index] += 1
        
        if s_left != s_right:
            mid = s_left + (s_right - s_left) // 2
            self.update(2*index+1, s_left, mid, target)
            self.update(2*index+2, mid+1, s_right, target)
        
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
        st, n, offset = SegmentTree(nums), len(nums), 10**4
        result = [0] * n
        
        for i in range(n-1, -1, -1):
            result[i] = st.query(0, 0, 2 * offset, nums[i]+offset)
            st.update(0, 0, 2 * offset, nums[i]+offset)
        
        return result