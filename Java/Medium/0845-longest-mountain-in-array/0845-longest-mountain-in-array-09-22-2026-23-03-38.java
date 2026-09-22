class Solution {
    public int longestMountain(int[] arr) {
        /*
        - increasing -> peak -> desc
        - longest subarray - variable sliding window
        - mountain -> valley - peak - valley
        - return maxlength when we see a mountain
        - else 0
        - Tme - O(n)
        - Space - O(1)
        */
        int n = arr.length - 1;
        int maxLength = 0;
        for(int i=1; i<n; i++) {
            if(arr[i-1] < arr[i] && arr[i] > arr[i+1]) {
                int left = i;
                int right = i;

                while(left > 0 && (arr[left-1]) < arr[left]) {
                    left--;
                }

                while(right < n && (arr[right] > arr[right+1])) {
                    right++;
                }

                maxLength = Math.max(right-left+1, maxLength);
            }
        }
        return maxLength;
    }
}