class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [None]*self.n
        self.visited = [False]*self.n

    def insert(self, idKey: int, value: str) -> List[str]:
        result = []
        self.stream[idKey-1] = value
        
        for i in range(len(self.stream)):
            val = self.stream[i]
            if self.visited[i]:
                continue
            if val == None:
                return result
            result.append(val)
            self.visited[i] = True
            
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

'''
- if you see an insert, insert the value and into that part of the array
    - so when you want to retrieve the values from the array i am storing everything,
    - example 1
    
    keep an array to list all the values returned
    [0, 0, 0, 0, 0]
    -insert [3, 'ccccc']
        - [0, 0, [3, 'ccccc'], 0, 0] -> return [] cos 0 till 3 is not ready yet, so basically loop through the array
        
    - insert [1, 'aaaaa']
        - [[1, 'aaaaa'], 0, [3, 'ccccc'], 0, 0] -> return [1, 'aaaaa'] cos that' the only one completely ready
    
    - insert [2, 'bbbbb']
        - [[1, 'aaaaa'], [2, 'bbbbb'], [3, 'ccccc'], 0, 0] -> return [2, 3]
        - visited = [true, true, true]
        
    - insert [5, 'eeeee']
        - [[1, 'aaaaa'], [2, 'bbbbb'], [3, 'ccccc'], 0, [5, 'eeeee']] -> return []
        - while i < len(arr)
            - if visited == true:
            continue
            - if val == 0:
            break
            - add to result array
'''