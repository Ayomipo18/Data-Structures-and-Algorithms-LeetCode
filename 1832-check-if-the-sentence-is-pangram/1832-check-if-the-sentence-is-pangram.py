class Solution:
    '''
    create an array of length 26 because we are dealing with only lower case english letters
    then go though the input string and for each char, put its freq in the array
    then go through the array and if any char is zero, retunr false, else true
    time - O(n)
    space - O(1)
    where n is the length of input string
    '''
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_count = [0] * 26
        
        for letter in sentence:
            key = ord(letter) - ord('a')
            alphabet_count[key] += 1
            
        for alphabet in alphabet_count:
            if alphabet == 0:
                return False
            
        return True