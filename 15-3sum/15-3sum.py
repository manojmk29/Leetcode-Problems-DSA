class Solution:
    def threeSum(self, nums):
        n=len(nums)
        nums.sort()
        result=[]
        i=0
        while(i<n-2):
            l=i+1
            r=n-1
            while (l<r):
                total=nums[i]+nums[l]+nums[r]
                if total>0:
                    r=r-1
                elif total<0:
                    l=l+1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while(l+1<n and nums[l+1]==nums[l]):
                        l+=1
                    l+=1
                    while(r-1>=0 and nums[r-1]==nums[r]):
                        r-=1
                    r-=1
            while(i+1<n and nums[i]==nums[i+1]):
                i+=1
            i+=1
        return(result)
                        
        