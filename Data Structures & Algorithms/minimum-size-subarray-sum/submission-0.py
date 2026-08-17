class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        L = 0
        currSum = 0
        for R in range(len(nums)):
            currSum += nums[R]

            while(currSum - nums[L] >= target):
                currSum -= nums[L]
                L += 1

            if(currSum >= target):
                res = min(res, R-L+1)

        return res if res != float("inf") else 0
        