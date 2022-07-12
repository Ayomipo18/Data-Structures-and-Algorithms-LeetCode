public class Solution {
    public bool Makesquare(int[] matchsticks) {
        if(matchsticks.Length == 0) return false;
        Array.Sort(matchsticks, Comparer<int>.Create((x,y) => y.CompareTo(x)));
        int maxSideLength = matchsticks.Sum() / 4;
        int[] sidesArray = new int[4];
        return dfs(matchsticks, 0, maxSideLength, sidesArray);
    }
    
    public bool dfs(int[] matchsticks, int index, int maxSideLength, int[] sidesArray) {
        if(index == matchsticks.Length) {
            return sidesArray[0] == sidesArray[1] && sidesArray[1] == sidesArray[2] && sidesArray[2] == sidesArray[3];
        }
        
        for(int i = 0; i < 4; i++) {
            if(sidesArray[i] + matchsticks[index] <= maxSideLength ) {
                sidesArray[i] += matchsticks[index];
                if(dfs(matchsticks, index+1, maxSideLength, sidesArray))
                    return true;
                sidesArray[i] -= matchsticks[index];
            }    
        }
        
        return false;
    }
}