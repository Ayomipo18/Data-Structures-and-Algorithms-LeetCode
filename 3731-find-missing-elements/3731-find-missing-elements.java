class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        Set<Integer> set = new HashSet<Integer>();
        int minVal = nums[0];
        int maxVal = nums[0];

        for(int num : nums) {
            set.add(num);
            minVal = Math.min(minVal, num);
            maxVal = Math.max(maxVal, num);
        }

        while(minVal < maxVal) {
            ++minVal;
            if(!set.contains(minVal)) {
                result.add(minVal);
            }
        }
        return result;
    }
}