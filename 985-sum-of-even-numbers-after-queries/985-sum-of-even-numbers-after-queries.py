class Solution:
    #time - O(max(nums.length, queries.length))
    #space - O(queries.length)
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        sum = 0
        for value in nums:
            if value % 2 == 0:
                sum += value
        
        for query in queries:
            prev_value = nums[query[1]]
            curr_value = query[0] + prev_value
            if prev_value % 2 == 0:
                sum -= prev_value
            if curr_value % 2 == 0:
                sum += curr_value
            nums[query[1]] = curr_value
            result.append(sum)

        return result