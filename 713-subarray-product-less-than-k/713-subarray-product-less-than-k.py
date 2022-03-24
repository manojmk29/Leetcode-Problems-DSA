class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        cur=1
        left=0
        ret=0
        n=len(nums)
        for right in range(len(nums)):
            cur*=nums[right]
            while(cur>=k and left<right):
                cur/=nums[left]
                left+=1
            if(nums[right]<k):
                ret+=right-left+1
        return(ret)
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if k <= 1: return 0
        # prod = 1
        # ans = left = 0
        # for right, val in enumerate(nums):
        #     prod *= val
        #     while prod >= k:
        #         prod /= nums[left]
        #         left += 1
        #     ans += right - left + 1
        # return ans