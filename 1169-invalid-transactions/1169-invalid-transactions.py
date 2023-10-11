class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        '''
        - result = []
        - i can split each string by the commas
        - then i can always check any transaction if it's more than 1000 dollars, push into my result array
        - also i want a check if the time is in range of 60 mins from the prev value
        - so meaning, i want to sort by name, then time
        - then always compare with the prev value to make sure it's same name, it's within 60 mins range and it's a diff city
        
        - put my data in the correct format i can use -> ["alice", 20, 800, "mtv"]
        - then sort by name and if name are equal, sort by time
        - then do the comparisms atsted above
            - i will say if a value is an invalid transaction and not in set already, add it
            - doesn't even matter, cos set will make it unique
            
        time complexity - O(nlogn) + O(n*n)
        space - O(nlogn) + O(n)
        '''
        
        result = []
        hashmap = {}
        m = len(transactions)
        
        for val in transactions:
            new_val = val.split(",")
            name = new_val[0]
            
            if name not in hashmap:
                hashmap[name] = []
                
            hashmap[name].append(Transaction(new_val[0], int(new_val[1]), int(new_val[2]), new_val[3]))
        
        for i in range(m):
            new_val = transactions[i].split(",")
            new_transaction = Transaction(new_val[0], int(new_val[1]), int(new_val[2]), new_val[3])
            if new_transaction.amount > 1000:
                result.append(new_transaction.convertToString())
            else:
                h_transaction = hashmap[new_transaction.name]
                for j in range(len(h_transaction)):
                    if new_transaction.name == h_transaction[j].name and abs(new_transaction.time - h_transaction[j].time) <= 60 and new_transaction.city != h_transaction[j].city:
                        result.append(new_transaction.convertToString())
                        break
            
        return result
    
class Transaction:    
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = time
        self.amount = amount
        self.city = city
        
    def convertToString(self):
        return self.name + ',' + str(self.time) + ',' + str(self.amount) + ',' + self.city