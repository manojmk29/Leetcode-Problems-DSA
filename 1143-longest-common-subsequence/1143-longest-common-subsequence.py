class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        @lru_cache(None)
        def helper(ai,bi):
            ret=left=right=0
            if(text1[ai]==text2[bi]):
                ret=1
                if(ai+1<=m-1 and bi+1<=n-1):
                    ret+=helper(ai+1,bi+1)
            else:
                if(ai+1<=m-1):
                    left=helper(ai+1,bi)
                if(bi+1<=n-1):
                    right=helper(ai,bi+1)   
            return(ret+max(left,right))
        return(helper(0,0))