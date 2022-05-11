#binary search
import bisect
class Solution:
    def lengthOfLIS(self,nums):
        arr=[]
        n=len(nums)
        for ind in range(n):
            val=bisect.bisect_left(arr,nums[ind])
            if(val==len(arr)):
                arr.append(nums[ind])
            else:
                arr[val]=nums[ind]
        return(len(arr))
                        