class Solution {
    public int maxArea(int[] height) {
        /*
        - max container area
        - combine diff container area
            - so how do i do that?
            - i pick the first and second, firs and third etc
            - cool, resolved
        - then max container area
            - so basically, after all of the above is done, i want to get the max of everything
            - but that is a O(n^2)
        - So how can i get the max container area without doing any of the combination
            - So basically, i get the max from the left
            - then i get the max from the right
            - i check the combination by using the lowest height x (dist between i1 and i2), then i compare max area and store the state
            - that's one combination, how do i compare next combination?
            - Next combination is I compare left and right heights
            - if left is less, we should move it else move right.
            - That's how we solve the problem
        - what can break this? - if array is empty, so make the check
        - area here is height x i
        - 
        */

        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;

        while(left < right) {
            int curWidth = (right - left);
            int curHeight = Math.min(height[left], height[right]);
            int curArea = curWidth * curHeight;
            maxArea = Math.max(maxArea, curArea);

            if (height[left] <= height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return maxArea;
    }
}