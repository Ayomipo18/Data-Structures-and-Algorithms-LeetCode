public class Solution {
    private IList<string> result = new List<string>();
    public IList<string> RestoreIpAddresses(string s) {
        Backtracking(new StringBuilder(s), 0, 0, 0);
        return result;
    }
    
    private void Backtracking(StringBuilder sb, int usedDots, int start, int prevDotIndex){
        if(usedDots==3){
            string address = sb.ToString();
            if(IsValidAddress(address)){
                result.Add(address);
            }
        }
        else{
            for(int i=start;i<sb.Length;i++){
                int addIndex = i;
                if (addIndex - prevDotIndex > 4 || addIndex - prevDotIndex < 1) continue;
                
                sb.Insert(addIndex, '.');
                Backtracking(sb, usedDots+1, i+1, addIndex);
                sb.Remove(addIndex,1);
            }
        }
    }
    
    private bool IsValidAddress(string str){
        string[] arr = str.Split('.');
        foreach(string item in arr){
            //returns false when number has pattern 0x...
            if(item.Length>1 && item[0]=='0') return false;
            
            //returns false when number is out of range [0,255]
            int num;
            if (!int.TryParse(item, out num)) return false;
            if (num < 0 || num > 255) return false;
        }
        return true;
    }
}