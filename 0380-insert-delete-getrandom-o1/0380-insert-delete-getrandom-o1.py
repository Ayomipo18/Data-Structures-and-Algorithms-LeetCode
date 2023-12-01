class RandomizedSet:
    '''
    - we are using a numMap to store list of values and also the values should map to the indexes in our numList
    - we are using the numList to store our vlaues also, an be able to get a random value(list can give random index and point to a value)
    - Also, when we are deleting a value from our entire system, we simply replace the value to be replaced in the numList with the val at the end of the numList and pop the value at the end of the numList.
    - Also, we use the del operator to delete the val from the numMap
    - Time complexity - O(1)
    - space - O(n)
    '''
    def __init__(self):
        self.numList = []
        self.numMap = {}

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numList.append(val)
            self.numMap[val] = len(self.numList)-1
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numList
        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        
        return res
        
    def getRandom(self) -> int:
        return random.choice(self.numList)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()