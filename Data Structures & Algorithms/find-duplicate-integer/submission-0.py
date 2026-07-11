class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numCnt = {}
        for num in nums:
            if numCnt.get(num, 0) != 0:
                return num
            else:
                numCnt[num] = 1
                
        