public class Solution {
    public int Fib(int n) {
        int fibPrev = 0;
        int fibCurr = 1;
        if(n == 0) return fibPrev;
        if(n == 1) return fibCurr;
        
        for(int i = 2; i<=n; i++) {
            int temp = fibCurr;
            fibCurr += fibPrev;
            fibPrev = temp;
        }
        
        return fibCurr;
    }
}