class Solution {
    public int smallestNumber(int n, int t) {
        //just bacially simulate it
        while(true) {
            if ((getDigitProduct(n) % t) == 0) {
                return n;
            }
            n++;
        }
    }

    public int getDigitProduct(int num) {
        int product = 1;
        while(num > 0) {
            product *= (num % 10);
            num /= 10;
        }

        return product;
    }
}