class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[-1 for i in range(n)]
        dp[-1]=0
        for i in range(n-2,-1,-1):
            t=float("inf")
            for j in range(i+nums[i],i,-1):
                if(j>=n-1):
                    v=0
                else:
                    v=dp[j]
                t=min(t,v+1)
            dp[i]=t
        return(dp[0])
                
        
        # n=len(nums)
        # dp=[-1 for i in range(n)]
        # for i in range(n):
        #     if(nums[i]==0):
        #         dp[i]=float("inf") 
        # dp[-1]=0
        # def helper(pos):
        #     if(dp[pos]!=-1):
        #         return(dp[pos])
        #     v=nums[pos]+pos
        #     dp[pos]=float("inf")
        #     for i in range(v,pos,-1):
        #         if(i>=n-1):
        #             dp[pos]=1
        #             break
        #         else:
        #             if(dp[i]==-1):
        #                 helper(i)
        #             dp[pos]=min(dp[pos],1+dp[i])
        #     return(dp[pos])
        # helper(0)
        # return(dp[0])
                        