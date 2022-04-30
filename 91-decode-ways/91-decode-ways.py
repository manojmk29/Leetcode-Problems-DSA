from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[-1 for i in range(n+1)]
        dp[n]=1
        def helper(ind):
            if(dp[ind]!=-1):
                return(dp[ind])
            if(s[ind]=="0"):
                dp[ind]=0
                return(0)
            tot=0
            tot+=helper(ind+1)
            if(ind+1<n):
                if(s[ind]=="1" or ( s[ind]=="2" and s[ind+1]<"7")):
                    tot+=helper(ind+2)
            dp[ind]=tot
            return(tot)
        return(helper(0))
    
    


# from functools import lru_cache
# class Solution:
#     @lru_cache
#     def numDecodings(self, s: str) -> int:
#         n=len(s)
#         def helper(ind):
#             if(ind==n):
#                 return(1)
#             if(s[ind]=="0"):
#                 return(0)
#             tot=0
#             tot+=helper(ind+1)
#             if(ind+1<n):
#                 if(s[ind]=="1" or ( s[ind]=="2" and s[ind+1]<"7")):
#                     tot+=helper(ind+2)
#             return(tot)
#         return(helper(0))