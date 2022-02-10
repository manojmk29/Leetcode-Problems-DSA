class Solution(object):
    def nextPermutation(self, nums):
        def reverse(s,e):
            while(s<e):
                nums[s],nums[e]=nums[e],nums[s]
                e-=1
                s+=1
        def swap(l,r):
            nums[l],nums[r]=nums[r],nums[l]
        n=len(nums)
        if(n==1):
            reverse(0,n-1)
            return
        i=n-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
        if(i==-1):
            reverse(0,n-1)
            return
        val=nums[i]
        j=i
        i=n-1
        while(i>0):
            if(nums[i]>nums[j]):
                swap(i,j)
                break
            else:
                i-=1
        reverse(j+1,n-1)
        