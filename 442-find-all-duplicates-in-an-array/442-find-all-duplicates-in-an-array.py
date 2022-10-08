class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        
        for i, val in enumerate(nums):
            val = abs(val)
            if nums[val - 1] < 0:
                result.append(val)
            else:
                nums[val - 1] = -nums[val - 1]
        
        return result
            
        
#sorting was helping me group numbers together, same as hashmap
#[4,3]
#each value in array corres to an index
#check at second value seeing and do something before then

#[0,1,2,3,4,5,6,7]

#[-4,-3,-2,-7,8,2,-3,-1]

#[2,3]

#go thru each value in my array, treat each value as an index itslef
#mark each index value, if it has been marked, push to array