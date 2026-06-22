class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        b = len(s)-1

        if not s[f].isalnum():
            f += 1
        if not s[b].isalnum():
            b -= 1
        while f < b:
            if s[f].lower() != s[b].lower():
                return False
            
            f += 1
            b -= 1
            while not s[f].isalnum():
                f += 1
            while not s[b].isalnum():
                b -= 1

        return True

        