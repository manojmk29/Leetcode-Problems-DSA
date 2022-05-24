class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        n=len(nums)
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        l=0
        for i in range(n//2):
            nums[l]=pos[i]
            nums[l+1]=neg[i]
            l+=2
        return(nums)
                
            
        