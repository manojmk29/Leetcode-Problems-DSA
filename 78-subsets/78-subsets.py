class Solution(object):
    def subsets(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n=len(nums)
        ret=[]
        def f1(ind,sub):
            ret.append(sub)
            for i in range(ind,n):
                f1(i+1,sub+[nums[i]])
        f1(0,[])
        return(ret)
    
        # ans=[]
        # first=[]
        # n=len(nums)
        # def helper(pos,arr):
        #     if(pos==n):
        #         ans.append(arr[:])
        #         return
        #     arr+=[nums[pos]]
        #     helper(pos+1,arr)
        #     arr.pop()
        #     helper(pos+1,arr)
        # helper(0,first)
        # return(ans)
        
        
        
        # res=[[]]
        # for num in nums:
        #     ans=[]
        #     for i in res:
        #         ans.append(i+[num])
        #     res+=ans
        # return(res)
        
        # def helper(pos,res=[[]]):
        #     if(pos<len(nums)):
        #         num=nums[pos]
        #         arr=[]
        #         for i in res:
        #             arr.append(i+[num])
        #         res+=arr
        #         return(helper(pos+1,res))
        #     else:
        #         return(res)
        # return(helper(0))