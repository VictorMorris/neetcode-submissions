class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCnt = defaultdict(int)
        for num in nums:
            if numCnt[num] != 0:
                return True
            numCnt[num] += 1
        return False