class Solution:
    '''
    solution 1
    - we can go through each str in strs
    - we sort each word and put it in an hashmap
    - then add the string to its corresponding hashmap key
    - at the end return hashmap.values()
    time - O(m*klogk)
    m is the length of strs array
    k is the max length of word
    
    solution 2
    - we can go through each str in strs
    - we create an array to keep count of each character in our str
    - we convert this array to a tuple
    - use the tuple as a key in our hashmap and append str that match our hashmap key
    - return hashmap.values()
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        # for str_val in strs:
        #     key = ''.join(sorted(str_val))
        #     result[key].append(str_val)
        
        for str_val in strs:
            count = [0] * 26
            for s in str_val:
                count[ord(s)-ord('a')] += 1
            result[tuple(count)].append(str_val)
            
        return result.values()