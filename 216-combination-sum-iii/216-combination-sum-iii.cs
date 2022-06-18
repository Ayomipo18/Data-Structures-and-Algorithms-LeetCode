public class Solution {
    public IList<IList<int>> CombinationSum3(int k, int n) {
        List<IList<int>> result = new List<IList<int>>();
        int total = 0;
        int number = 1;
        generateCombination(k, n, new List<int>(), total, number, result);
        return result;
    }
    
    void generateCombination(int k, int n, List<int> currArr, int total, int number, List<IList<int>> result) {
        if(currArr.Count == k) {
            if(total == n) {
                result.Add(new List<int>(currArr));
            }
            return;
        }
        for(int i = number; i<=9; i++) {
            currArr.Add(i);
            total += i;
            generateCombination(k, n, currArr, total, i + 1, result);
            currArr.Remove(i);
            total -= i;
        }
    }
}