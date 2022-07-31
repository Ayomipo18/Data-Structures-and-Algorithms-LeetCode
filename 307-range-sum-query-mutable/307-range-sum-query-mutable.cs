public class NumArray {

    int[] nums = null;
    int total = 0;
    int n = 0;
    public NumArray(int[] nums) {
        this.nums = nums;
        n = nums.Length;
        for (int i = 0; i < nums.Length; i++)
            total+=nums[i];
    }
    
    public void Update(int index, int val) {
        total -= nums[index];
        total += val;
        nums[index] = val;
    }
    
    public int SumRange(int left, int right) {
        var length = right - left;
        if (length < n/2)
        {
            var sum = 0;        
            for (int i = left; i <= right; i++)
                sum+=nums[i];

            return sum;
        }       
       
        int sumLeft = 0;        
        for (int i = 0; i < left; i++)
            sumLeft+=nums[i];
        
        int sumRight = 0;        
        for (int i = n-1; i > right; i--)
            sumRight+=nums[i];
        
        return total - sumLeft - sumRight;
        
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.Update(index,val);
 * int param_2 = obj.SumRange(left,right);
 */