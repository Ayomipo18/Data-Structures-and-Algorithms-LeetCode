class BIT:
    def __init__(self, n):
        self.sums = [0] * (n+1)
    
    def update(self, i, v):
        while i < len(self.sums):
            self.sums[i] += v
            i += i & -i
            
    def query(self, i):
        result = 0
        while i > 0:
            result += self.sums[i]
            i -= i & -i
        return result
        
class NumArray:
    """
    Implementation of Binary Indexed Tree/Fenwick Tree

    Memory:
        creation - O(n)
        update   - O(1)
        get_sum  - O(1)

    Time:
        creation - O(n*log(n))
        update   - O(log(n))
        get_sum  - O(log(n))
        
        where n is the length of nums
    """
    def __init__(self, nums: List[int]):
        self.b = BIT(len(nums))
        self.nums = nums
        for i, v in enumerate(nums):
            self.b.update(i+1, v)
        
    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.b.update(index+1, delta)
        self.nums[index] = val
        
    def sumRange(self, left: int, right: int) -> int:
        return self.b.query(right+1) - self.b.query(left)
            
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)