class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        /*
        - frequent elements - hashmap
        - most frequent elements - means elements should be retrieved in desc order
        - k most frequent - k elements frequency retrieved in desc order
        - Challenge -> Don't sort, so we don't want a complexity as O(nlogn)
        - Input: nums = [1,1,1,2,2,3], k = 2
        - Output: [1,2]
        - [3:1, 2:2, 1:3]
        - so what do i use when i want retrieve elems freq in desc order
            - i can use a heap -> real time sorting -> then get top k
            - i can use an hashmap -> into an arr/sort the values -> then get top k
        - I need an O(n) solu
            - ans is unique - anytime ans is unique, greedy style ans i think
            - k is in range [1, no of unique elems in the arr]
            - it's not sorted - so i can't use two pointers
            - what if i mantained a real time freq update of nums
                - this means
            - so my solu is basically frquency buckets
                - i keep a count of elems with an hashmap
                - but then i create buckets where each freq is its index and i start from the end of the bucket as i know that it's in desc order

        - Time - O(n)
        - Space - O(n)
        */

        int n = nums.length;
        HashMap<Integer, Integer> nums_hashmap = new HashMap<Integer, Integer>();
        List<Integer>[] buckets = new List[n + 1];

        for (int i = 0; i <= n; i++) {
            buckets[i] = new ArrayList<>();
        }

        for(int i=0; i<n; i++) {
            int val = nums[i];
            nums_hashmap.put(val, nums_hashmap.getOrDefault(val, 0)+1);
        }

        for(Map.Entry<Integer, Integer> entrySet : nums_hashmap.entrySet()) {
            buckets[entrySet.getValue()].add(entrySet.getKey());
        }

        int[] result = new int[k];
        int index = 0;

        for (int i = buckets.length - 1; i >= 0 && index < k; i--) {
            for (int num : buckets[i]) {
                result[index++] = num;
                if (index == k) {
                    return result;
                }
            }
        }

        return result;

    }
}