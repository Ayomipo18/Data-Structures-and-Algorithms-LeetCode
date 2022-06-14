public class Solution {
    public int Trap(int[] height) {
        int total = 0, leftPointer = 0, rightPointer = height.Length-1, leftMax = height[0], rightMax = height[height.Length-1];
        while(leftPointer < rightPointer) {
            if(height[leftPointer] <= height[rightPointer]) {
                if(leftMax > height[leftPointer]) {
                    total += leftMax - height[leftPointer];
                }
                else {
                    leftMax = height[leftPointer];
                }
                leftPointer++;
            }
            else {
                if(rightMax > height[rightPointer]) {
                    total += rightMax - height[rightPointer];
                }
                else {
                    rightMax = height[rightPointer];   
                }
                rightPointer--;
            }
        }
        return total;
    }
}