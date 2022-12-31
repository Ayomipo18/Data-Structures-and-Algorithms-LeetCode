class Solution:

    def __init__(self, w: List[int]):
        prefix_sum = 0
        self.weights = []

        for val in w:
            prefix_sum += val
            self.weights.append(prefix_sum)

        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = random.random() * self.total
        l, r = 0, len(self.weights)-1
        while l < r:
            mid = l + (r-l)//2
            if self.weights[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()