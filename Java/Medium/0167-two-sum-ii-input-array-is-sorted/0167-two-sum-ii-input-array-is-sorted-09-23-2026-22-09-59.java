class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /*
        - 1-indexed array of integers numbers sorted in non-desc order
        - find number and its complement
        - its sorted, so we use greedy, 2 pointers
        - we have criterias
            - mathematical expressions
             if arr[left] + arr[right] > target, right--
             if arr[left] + arr[right] < target, left--;
        - Time - O(n)
        - Space - O(1)
        */

        int left = 0;
        int right = numbers.length - 1;

        while(left < right) {
            int curSum = numbers[left] + numbers[right];
            if(curSum > target) {
                right--;
            } else if (curSum < target) {
                left++;
            } else {
                return new int[]{left+1, right+1};
            }
        }

        return new int[2];
    }
}