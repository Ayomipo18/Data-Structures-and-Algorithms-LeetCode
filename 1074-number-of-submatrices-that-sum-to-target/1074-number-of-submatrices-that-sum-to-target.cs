public class Solution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) {
        for(int i=0; i< matrix.Length; i++){
            for(int j=1; j< matrix[0].Length; j++){
                matrix[i][j] += matrix[i][j-1]; 
            }
        }
        int counter = 0;
        //this loop will remove previous column by 1 so that remaining columns will be checked
        for(int col1=0; col1 < matrix[0].Length; col1++){
            //this loop will be used to check the column starting from above and ending till end
            for(int col2=col1; col2< matrix[0].Length; col2++){
                Dictionary<int,int> records = new Dictionary<int,int>();
                records[0] = 1;
                int sum = 0;
                for(int row=0; row < matrix.Length; row++){
                    sum += matrix[row][col2] - (col1 > 0 ? matrix[row][col1-1] : 0);
                    int prefixSum = sum - target;
                    if(records.ContainsKey(prefixSum)){
                        counter += records[prefixSum];
                    }
                    if(records.ContainsKey(sum))
                        records[sum] += 1;
                    else
                    records[sum] = 1;
                    
                }
            }
        }
        return counter;
    }
}