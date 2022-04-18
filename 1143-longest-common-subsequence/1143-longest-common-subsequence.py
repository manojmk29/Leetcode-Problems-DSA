class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        @lru_cache(None)
        def helper(a,b):
            ret=left=right=0
            if(text1[a]==text2[b]):
                ret=1
                if(a-1>=0 and b-1>=0):
                    ret+=helper(a-1,b-1)
                return(ret)
            if(a-1>=0):
                left=helper(a-1,b)
            if(b-1>=0):
                right=helper(a,b-1)
            val=max(left,right)
            return(val)
        return(helper(m-1,n-1))
            
            
#         m=len(text1)
#         n=len(text2)
#         @lru_cache(None)
#         def helper(ai,bi):
#             ret=left=right=0
#             if(text1[ai]==text2[bi]):
#                 ret=1
#                 if(ai+1<=m-1 and bi+1<=n-1):
#                     ret+=helper(ai+1,bi+1)
#             else:
#                 if(ai+1<=m-1):
#                     left=helper(ai+1,bi)
#                 if(bi+1<=n-1):
#                     right=helper(ai,bi+1)   
#             return(ret+max(left,right))
#         return(helper(0,0))