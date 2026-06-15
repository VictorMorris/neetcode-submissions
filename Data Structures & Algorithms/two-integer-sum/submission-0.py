class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIdx = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in numIdx.keys():
                return [numIdx[t], i]
            numIdx[nums[i]] = i
