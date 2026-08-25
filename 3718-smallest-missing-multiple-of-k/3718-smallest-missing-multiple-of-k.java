class Solution {
    public int missingMultiple(int[] nums, int k) {
        /*
        - This is a smallest multiple simulation and hashset lookup
        - Time - O(n)
        - Space - O(n)
        */

        HashSet<Integer> set = new HashSet<Integer>();

        for(int num: nums) {
            set.add(num);
        }

        int i = 1;
        while(i<=nums.length) {
            int missingMultiple = i*k;

            if (!set.contains(missingMultiple)) {
                return missingMultiple;
            }

            i++;
        }

        return i*k;
    }
}