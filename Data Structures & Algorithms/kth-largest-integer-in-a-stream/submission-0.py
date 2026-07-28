class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
        

    def add(self, val: int) -> int:
        for i in range(len(self.nums) + 1):
            if i == len(self.nums):
                self.nums.append(val)
                return self.nums[-self.k]
            elif val < self.nums[i]:
                self.nums.insert(i, val)
                return self.nums[-self.k]

