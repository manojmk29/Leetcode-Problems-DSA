class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=i=0
        n=len(nums)
        r=n-1
        while(i<=r):
            if(nums[i]==0):
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
                i+=1
            elif(nums[i]==2):
                nums[r],nums[i]=nums[i],nums[r]
                r-=1
            else:
                i+=1