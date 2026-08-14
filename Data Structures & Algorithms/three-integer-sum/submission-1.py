class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for p1 in range(len(nums)):
            numMap = defaultdict(int)
            for i in range(p1 + 1, len(nums)):
                t = 0 - nums[p1] - nums[i]
                if numMap[t] > 0:
                    res.add(tuple(sorted((nums[p1], nums[i], t))))
                numMap[nums[i]] += 1

        return [list(triplet) for triplet in res]


        