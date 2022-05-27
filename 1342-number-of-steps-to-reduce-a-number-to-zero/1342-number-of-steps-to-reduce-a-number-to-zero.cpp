class Solution {
public:
    int numberOfSteps(int num) {
        int count = 0;
        while(num != 0) {
            if(num % 2 == 0) {
                num = num >> 1;
                count++;
            }
            else {
                num = subtract(num, 1);
                count++;
            }
        }
        return count;
    }
    
    int subtract(int x, int y) {
        while (y != 0) {
            int borrow = (~x) & y;
            x = x ^ y;
            y = borrow << 1;
        } 
        return x;
    }
};