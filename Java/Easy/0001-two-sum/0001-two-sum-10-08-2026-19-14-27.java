class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap();

        for (int i=0; i<nums.length; i++) {
            Integer num = nums[i];
            if (hashmap.containsKey(num)) {
                return new int[]{hashmap.get(num), i};
            }

            int num_to_find = target-num;
            hashmap.put(num_to_find, i);
        }

        return new int[2];
    }
}