class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0 for x in range(len(height))]
        maxRight = [0 for x in range(len(height))]
        trapped = 0

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        for i in range(0, len(height)):
            currTrapped = min(maxLeft[i], maxRight[i]) - height[i]
            if currTrapped > 0:
                trapped += currTrapped

        return trapped

        