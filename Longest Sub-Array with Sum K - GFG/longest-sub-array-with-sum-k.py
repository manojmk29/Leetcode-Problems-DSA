#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        #Complete the function
        ret=0
        dif=K
        hmap={}
        hmap[0]=0
        tot=0
        for ind,var in enumerate(A,1):
            tot+=var
            if(tot==dif):
                ret=max(ret,ind)
            if(tot-dif in hmap):
                ret=max(ret,ind-hmap[tot-dif])
            if(tot not in hmap):
                hmap[tot]=ind
        return(ret)
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))




# } Driver Code Ends