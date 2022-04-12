class Solution:
    def minDistance(self, word1: str, word2: str) :
        m=len(word1)
        n=len(word2)
        @lru_cache(None)
        def helper(i,j):
            if(i==0):
                return(j)
            if(j==0):
                return(i)
            if(word1[i-1]==word2[j-1]):
                return(helper(i-1,j-1))
            p=1+helper(i-1,j-1)
            q=1+helper(i,j-1)
            r=1+helper(i-1,j)
            return(min(p,q,r))
        return(helper(m,n))
        