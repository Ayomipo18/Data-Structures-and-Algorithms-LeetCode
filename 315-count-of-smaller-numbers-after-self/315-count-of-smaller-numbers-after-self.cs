public class Solution {
     public IList<int> CountSmaller(int[] nums)
        {
            var sorted = new List<int>();
            var res = new List<int>();
            for (int i = nums.Length - 1; i >= 0; i--)
            {
                var pos = BinarySearch(sorted, nums[i]);
                sorted.Insert(pos + 1, nums[i]);
                res.Add(pos + 1);
            }
            res.Reverse();
            return res;
        }
        public int BinarySearch(List<int> inputArray, int key)
        {
            int min = 0;
            int max = inputArray.Count - 1;
            while (min <= max)
            {
                int mid = (min + max) / 2;
                if (key <= inputArray[mid])
                {
                    max = mid - 1;
                }
                else
                {
                    min = mid + 1;
                }
            }
            return max;
        }
}