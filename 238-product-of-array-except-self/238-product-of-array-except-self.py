class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=[1]
        right=[1]
        prev=1
        for i in nums:
            left.append(prev*i)
            prev=left[-1]
        prev=1
        for i in nums[::-1]:
            right.append(prev*i)
            prev=right[-1]
        right.pop()
        right=right[::-1]
        ret=[]
        for i in range(len(nums)):
            ret.append(left[i]*right[i])
        return(ret)