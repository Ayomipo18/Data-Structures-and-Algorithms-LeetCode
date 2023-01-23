class Solution:
    '''
    solution 1
    - we can go through each str in strs
    - we sort each word and put it in an hashmap
    - then add the string to its corresponding hashmap key
    - at the end return hashmap.values()
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for str_val in strs:
            key = ''.join(sorted(str_val))
            result[key].append(str_val)
            
        return result.values()