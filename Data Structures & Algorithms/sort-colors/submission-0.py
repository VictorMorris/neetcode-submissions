class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorCnt = defaultdict(int)
        for n in nums:
            colorCnt[n] += 1

        nums[:] = [n for color in range(3) for n in [color] * colorCnt[color]]