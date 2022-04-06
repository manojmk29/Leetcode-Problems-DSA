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
        tar=abs(tot//2)
        n=len(nums)
        dp=[[-1 for i in range(tar+1)]for i in range(n)]
        def helper(ind,cur):
            if(dp[ind][cur]!=-1):
                return(dp[ind][cur])
            if(ind==0):
                if(cur==0 or cur-nums[ind]==0):
                    dp[ind][cur]=1+(nums[ind]==0)
                    return(1+(nums[ind]==0))
                else:
                    dp[ind][cur]=0
                    return(0)
            notake=helper(ind-1,cur)
            take=0
            if(cur-nums[ind]>=0):
                take=helper(ind-1,cur-nums[ind])
            dp[ind][cur]=notake+take
            return(notake+take)
        n=len(nums)
        return(helper(n-1,tar))