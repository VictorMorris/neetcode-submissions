class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        for i1 in range(len(nums)):
            for i2 in range(i1+1, (len(nums))):
                numMap = defaultdict(int)
                for n in range(i2+1, len(nums)):
                    t = target - nums[i1] - nums[i2] - nums[n]
                    if t in numMap.keys():
                        res.add(tuple(sorted((nums[i1], nums[i2], nums[n], t))))
                    numMap[nums[n]] += 1 

        return list(res)

        