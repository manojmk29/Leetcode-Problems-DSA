class Solution(object):
    def removeDuplicates(self, nums):
        val=nums[0]
        cnt=0
        ptr=0
        l=len(nums)
        k=0
        for i in range(l):
            if(val==nums[i]):
                cnt+=1
            else:
                val=nums[i]
                cnt=1
            if(cnt<=2):
                nums[ptr],nums[i]=nums[i],nums[ptr]
                ptr+=1
        return(ptr)