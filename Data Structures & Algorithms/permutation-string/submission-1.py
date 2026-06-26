class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Cnt = [0 for x in range(26)]
        s2Cnt = [0 for x in range(26)]

        for c in s1:
            s1Cnt[ord(c) - ord('a')] += 1

        i = 0
        while i < len(s2):
            c = s2[i]
            if i < len(s1):
                s2Cnt[ord(s2[i]) - ord('a')] += 1
            else:
                s2Cnt[ord(s2[i]) - ord('a')] += 1
                s2Cnt[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if s1Cnt == s2Cnt:
                return True
            i += 1

        return False

        