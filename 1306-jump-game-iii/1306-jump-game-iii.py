class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n=len(arr)
        f=[0 for i in range(len(arr))]
        def helper(start):
            if(start>n-1 or start<0 or f[start]==1):
                return(False)
            if(arr[start]==0):
                return(True)
            f[start]=1
            return(helper(start+arr[start]) or helper(start-arr[start]))
            # l=start+arr[start]
            # r=start-arr[start]
            # f[start]=1
            # if(l<0 or f[l]==1):
            #     l=False
            # else:
            #     helper(l)
            # if(l<0 or f[l]==1):
            #     l=False
            # else:
            #     l=helper(l)
            # if(r>n-1 or f[l]==1):
            #     r=False
            # else:
            #     r=helper(r)
            # if(l or r):
            #     return(True)
            # arr[start]=0
            # return(False)
        return(helper(start))
        
            
        