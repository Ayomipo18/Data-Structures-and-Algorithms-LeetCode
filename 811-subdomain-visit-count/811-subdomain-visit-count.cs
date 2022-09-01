public class Solution {
    //n = cpdomains.Length , where we assume that domain(cpdomains).Length is fixed
    //time complexity - O(n)
    //space complexity - O(n)
    public IList<string> SubdomainVisits(string[] cpdomains) {
        Dictionary<string, int> dict = new(); //O(n)
        
        foreach(string cpdomain in cpdomains) { //O(cpdomains.Length)
            string[] domainData = cpdomain.Split(" ");
            int count = Int32.Parse(domainData[0]);
            string domain = domainData[1]; //discuss.leetcode.com
            
            while(string.IsNullOrEmpty(domain) == false) { //O(domain.Length)
                if(!dict.ContainsKey(domain)) {
                    dict.Add(domain, count);
                }
                else dict[domain] += count;
                
                int dotIndex = domain.IndexOf('.'); //O(domain.Length)
                if(dotIndex < 0) domain = null;
                else domain = domain.Substring(dotIndex + 1); //O(domain.Length)
            } 
        }
        
        IList<string> result = new List<string>(capacity: dict.Count); //O(n)
        foreach(KeyValuePair<string, int> entry in dict) { //O(3 * domain.Length)
            result.Add($"{entry.Value} {entry.Key}");
        }
        
        return result;
        
    }
}

//create a dictionary<string, int>
//do a forloop through cpdomains
//foreach string in cpdomains, split with " "
//convert split[0] to integer
//then split the first split[1] by "."
//if(first split[1] is not in dictionary) add it, with split[0]
//else increase with split[0]
//if(second split[2] is not in dictionary) add it, else increase with split[0]
//foreach key value pair in the dictionary, concat key and value with space and push to array