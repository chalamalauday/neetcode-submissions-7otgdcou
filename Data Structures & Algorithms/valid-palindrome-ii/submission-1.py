class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1]==s:
            return True
        for i in range(len(s)):
            ns=s[:i]+s[i+1:]
            if ns[::-1]==ns:
                return True
        return False
        