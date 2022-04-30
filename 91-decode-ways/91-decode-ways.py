from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1 for i in range(n+1)]
        dp[n]=1
        for ind in range(n-1,-1,-1):
            if(s[ind]=="0"):
                dp[ind]=0
            else:
                tot=0
                tot+=dp[ind+1]
                if(ind+1<n):
                    if(s[ind]=="1" or ( s[ind]=="2" and s[ind+1]<"7")):
                        tot+=dp[ind+2]
                dp[ind]=tot
        return(dp[0])