class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            w = i
            chrCnt = {}
            currLen = 0
            while w < len(s) and chrCnt.get(s[w],0) == 0:
                chrCnt[s[w]] = 1
                currLen += 1
                w += 1
            maxLen = max(currLen, maxLen)

        return maxLen
        