public class Solution {
    public string[] FindRestaurant(string[] list1, string[] list2) {
        List<string> result = new List<string>();
        
        Dictionary<string, int> dict = new Dictionary<string, int>();
        
        for(int i = 0; i < list1.Length; i++) {
            dict.Add(list1[i], i);
        }
        
        int min = int.MaxValue;
        
        int sum;
        
        for(int i = 0; i < list2.Length; i++) {
            if(dict.ContainsKey(list2[i])) {
                sum = dict[list2[i]] + i;
                if(sum < min) {
                    result = new List<string>();
                    result.Add(list2[i]);
                    min = sum;
                } else if (sum == min) {
                    result.Add(list2[i]);
                }
            }
        }
        
        return result.ToArray();
    }
}