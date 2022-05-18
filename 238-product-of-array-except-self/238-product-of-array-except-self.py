class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret=[]
        cur=1
        for i in nums:
            ret.append(cur)
            cur*=i
        cur=1
        for i in range(len(nums)-1,-1,-1):
            ret[i]*=cur
            cur*=nums[i]
        return(ret)
        