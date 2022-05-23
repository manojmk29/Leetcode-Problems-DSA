class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret=nums[0]
        cur=nums[0]
        for i in nums[1:]:
            cur=max(cur+i,i)
            ret=max(ret,cur)
        return(ret)
        