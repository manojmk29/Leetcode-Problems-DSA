class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=sum(nums)
        cur=0
        for i,j in enumerate(nums):
            if(cur==tot-j-cur):
                return(i)
            cur+=j
        return(-1)