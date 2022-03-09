class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret=[]
        for i in range(len(nums)):
            cnt=0
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    cnt+=1
            ret.append(cnt)
        return(ret)
                    
            
        