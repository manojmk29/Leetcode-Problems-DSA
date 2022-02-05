class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        hmax={}
        l=len(nums)
        if(l<3):
            return(False)
        hmax[l-1]=nums[l-1]
        for i in range(l-2,-1,-1):
            hmax[i]=max(nums[i],hmax[i+1])
        hmax2={}
        hmax2[0]=nums[0]
        for i in range(1,l-1):
            hmax2[i]=min(nums[i],hmax2[i-1])
        curr=nums[0]
        for i in range(1,l-1):
            if(hmax[i]>nums[i] and hmax2[i]<nums[i]):
                return(True)
        return(False)