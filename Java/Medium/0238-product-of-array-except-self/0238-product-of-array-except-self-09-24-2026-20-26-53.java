class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
        - return arr ans
        - ans[i] = product all elems of nums except nums[i]
        - this is an all element product except itself
        - so this is basically prefix product except itself
        - and becuase it's all sum except itself, we want to do a prefix product from both LHS and RHS then exclude itself
        - I will have two arrays
            - LHS prefix product
            - RHS prefix product
            - For each index, i will then add LHS[i-1] + RHS[i+1]
            - FOr the first and last value, i will do it diff as they don't have indexes to the left or right
        - O(n) time
        - O(n) space

        - How to do in O(1) Space
        - What am i doing with the curr O(n) space - I am doing LHS and RHS prefix product
        - I can't figure out the tech concept
        - The concept is output resuse + rolling variable
        - basically inplace LHS/RHS prefix product
        - but instead of using the cur val in the product, we use prefix/suffix, that's where the rolling sum comes in
        */

        int n = nums.length;
        int[] result = new int[n];
        int rollingProduct = 1;

        for(int i=0; i<n; i++) {
            result[i] = rollingProduct;
            rollingProduct *= nums[i];
        }

        rollingProduct = 1;
        for(int i=n-1; i>=0; i--) {
            result[i] *= rollingProduct;
            rollingProduct *= nums[i];
        }

        return result;
    }
}