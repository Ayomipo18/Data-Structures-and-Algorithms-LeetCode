class Solution:
	def goodIndices(self, nums: List[int], k: int) -> List[int]:
		if k == 1:
			return list(range(1, len(nums) - 1))
		res = []
		count = 1
		for i in range(1, len(nums) - k - 1):
			if nums[i] <= nums[i - 1] and nums[i + k + 1] >= nums[i + k]:
				count += 1
				if count >= k:
					res.append(i + 1)
			else:
				count = 1
            
		return res