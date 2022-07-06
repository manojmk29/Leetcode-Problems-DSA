# class Solution:
#     def canPartitionKSubsets(self, A, k):
#             if len(A) < k:
#                 return False
#             ASum = sum(A)
#             A.sort(reverse=True)
#             if ASum % k != 0:
#                 return False
#             target = [ASum / k] * k

#             def dfs(pos):
#                 if pos == len(A): return True
#                 for i in range(k):
#                     if target[i] >= A[pos]:
#                         target[i] -= A[pos]
#                         if dfs(pos + 1):
#                             return True
#                         target[i] += A[pos]
                        
#                 return False
#             return dfs(0)

class Solution:
    def canPartitionKSubsets(self,nums,k):
        tot=sum(nums)
        if tot % k != 0:
            return False
        need=tot//k
        n=len(nums)
        nums.sort(reverse=True)
        arr=[need for i in range(k)]
        for i in nums:
            if i > need:
                return False 
        def helper(ind):
            if(ind==n):
                return(True)
            for i in range(k):
                if(arr[i]>=nums[ind]):
                    arr[i]-=nums[ind]
                    if(helper(ind+1)):
                        return(True)
                    arr[i]+=nums[ind]
                    if(arr[i]==need):
                        break
            return(False)
        return(helper(0))
                
                    
            