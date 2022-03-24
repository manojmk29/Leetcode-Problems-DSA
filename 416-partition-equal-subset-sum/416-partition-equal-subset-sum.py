from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot=sum(nums)
        n=len(nums)
        if(tot%2!=0):
            return(False)
        need=tot//2
        @cache
        def helper(ind,a):
            if(a==need):
                return(True)
            if(a>need or ind>=n):
                return(False)
            return(helper(ind+1,a+nums[ind]) or helper(ind+1,a))
        return(helper(0,0))            
        