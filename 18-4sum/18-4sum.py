class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        ret=[]
        n=len(nums)
        if(n<4):
            return([])
        if(n==4):
            return [nums] if sum(nums)==target else []
        p=0
        while(p<n-3):
            q=p+1
            while(q<n-2):
                tot=nums[p]+nums[q]
                r=q+1
                s=n-1
                while(r<s):
                    val=tot+nums[r]+nums[s]
                    if(val>target):
                        s-=1
                    elif(val<target):
                        r+=1
                    else:
                        ret.append([nums[p],nums[q],nums[r],nums[s]])
                        rval=nums[r]
                        while(r<n and nums[r]==rval):
                            r+=1
                        sval=nums[s]
                        while(s>=0 and nums[s]==sval):
                            s-=1
                qval=nums[q]
                while(q<n and nums[q]==qval):
                    q+=1
            pval=nums[p]
            while(p<n and nums[p]==pval):
                p+=1
        return(ret) 