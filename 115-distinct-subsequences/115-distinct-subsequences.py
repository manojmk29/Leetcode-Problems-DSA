class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        @lru_cache(None)
        def helper(i,j):
            if(i==0 or j==0):
                return(0)
            nt=helper(i-1,j)
            tt=0
            if(s[i-1]==t[j-1]):
                if(j==1):
                    tt=1
                else:
                    tt=helper(i-1,j-1)
            return(nt+tt)
        val=helper(m,n)
        return(val)