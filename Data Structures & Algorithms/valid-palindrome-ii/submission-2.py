class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        if(s==s[::-1]):
            return True
        while l<r:
            if s[l]!=s[r]:
                nsl=s[l+1:r+1]
                nsr=s[l:r]
                return nsl==nsl[::-1] or nsr==nsr[::-1]
            l+=1
            r-=1
        return False
        