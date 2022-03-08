class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        one=zero=0
        ret=0
        start=0
        for ind,i in enumerate(nums):
            if i==0:
                zero+=1
            else:
                one+=1
            while(zero>k):
                if nums[start]==1:
                    one-=1
                else:
                    zero-=1
                start+=1
            ret=max(ret,ind-start+1)
        return(ret)