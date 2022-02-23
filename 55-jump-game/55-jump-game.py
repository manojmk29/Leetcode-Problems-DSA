class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        tgt=n-1
        temp=nums[0]
        if(tgt==0):
            return(True)
        for i in range(tgt):
            if(nums[i]==0 and temp<=i):
                return(False)
            temp=max(temp,i+nums[i])
            if(temp>=tgt):
                return(True)
        return(False)