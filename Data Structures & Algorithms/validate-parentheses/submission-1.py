class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        brackMap = {"(":")", "{":"}", "[":"]"}

        for c in s:
            if c in brackMap.keys():
                stack.append(c)
            elif c in brackMap.values():
                if stack:
                    opener = stack.pop()
                else:
                    return False
                if brackMap.get(opener, 0) != c:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        