class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxt=nums[0]
        le=len(nums)-1
        for i in range(len(nums)):
            if(maxt<i):
                return(False)
            maxt=max(maxt,i+nums[i])
            if(maxt>=le):
                return(True)