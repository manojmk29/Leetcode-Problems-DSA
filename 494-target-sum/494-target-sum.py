from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        """
        tot=sum(nums)
        s1-s2=d
        s2=tot-s1
        s1-tot+s1=d
        2s1-tot=d
        2s1=tot+d
        s1=tot+d//2
        """
        tot=sum(nums)
        tot+=target
        if(tot%2!=0):
            return(0)
        tar=tot//2
        tar=abs(tar)
        n=len(nums)
        dp=[[-1 for i in range(tar+1)]for i in range(n)]
        for cur in range(tar+1):
            if(cur==0 or cur-nums[0]==0):
                dp[0][cur]=1+(nums[0]==0)
            else:
                dp[0][cur]=0
        for ind in range(1,n):
            for cur in range(tar+1):
                notake=dp[ind-1][cur]
                take=0
                if(cur>=nums[ind]):
                    take=dp[ind-1][cur-nums[ind]]
                dp[ind][cur]=notake+take
        return(dp[n-1][tar])