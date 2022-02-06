class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ind=-1
        cnt=0
        l=len(nums)
        for i in range(l-1):
            if(nums[i]>nums[i+1]):
                if(ind==-1):
                    ind=i
                else:
                    return(False)
        return(ind==-1 or ind==0 or ind==l-2 or nums[ind-1]<=nums[ind+1] or nums[ind+2]>nums[ind])
            