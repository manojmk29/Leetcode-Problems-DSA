class Solution(object):
    def minSubarray(self, nums, p):
        tot=sum(nums)
        n=len(nums)
        if(tot%p==0):
            return(0)
        ret=float("inf")
        prev=0
        need=tot%p
        hmap={0:-1}
        for ind,val in enumerate(nums):
            prev+=val
            prev%=p
            if((prev-need)%p in hmap):
                dist=ind-hmap[(prev-need)%p]
                if(dist!=n):
                    ret=min(ret,dist)
            hmap[prev]=ind
        return(ret if(ret!=float("inf")) else -1)       