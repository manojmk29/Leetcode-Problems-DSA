class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot=sum(nums)
        n=len(nums)
        if(tot%2!=0):
            return(False)
        need=tot//2
        dp={}
        def helper(ind,a):
            if(a==need):
                return(True)
            if(a>need or ind>=n):
                return(False)
            if(a not in dp):
                dp[a]=helper(ind+1,a+nums[ind]) or helper(ind+1,a)
            return(dp[a])
        return(helper(0,0))            
        