class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> numsMap = new HashMap<Integer, Integer>();
        int[] result = new int[Math.min(nums1.length, nums2.length)];
        int k = 0;

        for (int num : nums1) {
            numsMap.put(num, numsMap.getOrDefault(num, 0)+1);
        }

        for (int num : nums2) {
            if (numsMap.getOrDefault(num, 0) > 0) {
                result[k++] = num;
                numsMap.put(num, numsMap.get(num) - 1);
            }
        }

        return Arrays.copyOf(result, k);
    }
}