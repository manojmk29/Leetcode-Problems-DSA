class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[0 for i in range(n+1)]for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                nt=dp[i-1][j]
                tt=0
                if(s[i-1]==t[j-1]):
                    if(j==1):
                        tt=1
                    else:
                        tt=dp[i-1][j-1]
                dp[i][j]=tt+nt
        return(dp[m][n])
    
    
#         @lru_cache(None)
#         def helper(i,j):
#             if(i==0 or j==0):
#                 return(0)
#             nt=helper(i-1,j)
#             tt=0
#             if(s[i-1]==t[j-1]):
#                 if(j==1):
#                     tt=1
#                 else:
#                     tt=helper(i-1,j-1)
#             return(nt+tt)
#         val=helper(m,n)
#         return(val)