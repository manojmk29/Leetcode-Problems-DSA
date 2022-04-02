class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        abdgfba
        """
        def helper(l,r,rem):
            if(l>=r):
                return(True)
            if(s[l]==s[r]):
                return(helper(l+1,r-1,rem))
            else:
                if rem>0:
                    return False
                return helper(l+1,r,rem+1) or helper(l,r-1,rem+1)
        return(helper(0,len(s)-1,0))