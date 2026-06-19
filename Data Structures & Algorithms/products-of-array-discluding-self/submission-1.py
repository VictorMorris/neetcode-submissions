class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(len(nums)-1):
            res.append(res[i]*nums[i])
        
        post = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * post
            post *= nums[i]

        return res

        