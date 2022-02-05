class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        arr=[1]*len(nums)
        for i in range(l-2,-1,-1):
            for j in range(i+1,l):
                if(nums[i]<nums[j]):
                    arr[i]=max(arr[i],1+arr[j])
        return(max(arr))
        
        
        
        
        #TLE
        
        # self.ret=1
        # mint=-float("inf")
        # def helper(ind,mint,count):
        #     self.ret=max(self.ret,count)
        #     if(ind==len(nums)):
        #         return
        #     val=nums[ind]
        #     helper(ind+1,mint,count)
        #     if(val>mint):
        #         mint=max(mint,val)
        #         helper(ind+1,mint,count+1)
        #     else:
        #         return
        # helper(0,mint,0)
        # return(self.ret)