class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = defaultdict(int)
        for c in s1:
            s1Map[c] += 1

        l = 0
        r = len(s1)
        s2Map = defaultdict(int)
        for c in s2[l:r]:
            s2Map[c] += 1
        
        while r < len(s2):
            if all(s2Map[c] == s1Map[c] for c in s1Map):
                return True
            s2Map[s2[l]] -= 1
            s2Map[s2[r]] += 1
            l += 1
            r += 1
        
        return all(s2Map[c] == s1Map[c] for c in s1Map)