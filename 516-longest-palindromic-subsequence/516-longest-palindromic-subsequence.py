class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
            text1=s
            text2=s[::-1]
            m=n=len(text1)
            prev=[0 for i in range(n+1)]
            cur=[0 for i in range(n+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if(text1[i-1]==text2[j-1]):
                        cur[j]=1+prev[j-1]
                    else:
                        cur[j]=max(prev[j],cur[j-1])
                prev=cur[:]
            return(prev[n])
        
#             @lru_cache(None)
#             def helper(ai,bi):
#                 ret=left=right=0
#                 if(text1[ai]==text2[bi]):
#                     ret=1
#                     if(ai+1<=m-1 and bi+1<=n-1):
#                         ret+=helper(ai+1,bi+1)
#                 else:
#                     if(ai+1<=m-1):
#                         left=helper(ai+1,bi)
#                     if(bi+1<=n-1):
#                         right=helper(ai,bi+1)   
#                 return(ret+max(left,right))
#             return(helper(0,0))
        