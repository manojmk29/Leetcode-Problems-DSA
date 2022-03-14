class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=[0]
        for i in range(len(nums)-1):
            first.append(first[-1]+nums[i])
        second=[0]
        for i in range(len(nums)-1,0,-1):
            second.append(second[-1]+nums[i])
        second=second[::-1]
        for i in range(len(nums)):
            if(first[i]==second[i]):
                return(i)
        return(-1)
        
            