class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            if not stack or heights[i] > stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                while stack and heights[i] <= stack[-1][1]:
                    res = max(res, stack[-1][1]*(i-stack[-1][0]))
                    lastIdx = stack[-1][0]
                    stack.pop()
                stack.append((lastIdx, heights[i]))
        while stack:
            idx, h = stack.pop()
            res = max(res, h * (len(heights) - idx))
        return res

"""
stack = [(0,1), (2, 2)]
res = 7
lastIdx = 2
i = 5

"""

        