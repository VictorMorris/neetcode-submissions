class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for x in range(len(temperatures))]
        stack = collections.deque()

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                tempIdx = stack.pop()
                res[tempIdx] = i-tempIdx
            stack.append(i)

        return res
        