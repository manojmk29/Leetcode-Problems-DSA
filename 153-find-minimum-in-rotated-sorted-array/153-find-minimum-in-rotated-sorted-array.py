class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        ret=nums[0]
        while(l<=r):
            mid=(l+r)//2
            if(nums[l]<=nums[mid]):
                ret=min(ret,nums[l])
                l=mid+1
            else:
                ret=min(ret,nums[mid])
                r=mid-1
        return(ret)