class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tgt=len(nums)-1
        temp=nums[0]
        for i in range(tgt):
            if(temp<i):
                return(False)
            temp=max(temp,i+nums[i])
            if(temp>=tgt):
                return(True)
        return(temp>=tgt)