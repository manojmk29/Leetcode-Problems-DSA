#User function Template for python3
from functools import lru_cache
class Solution:
    def knapSack(self,W, wt, val, n):
        # @lru_cache(None)
        dp=[[-1 for i in range(W+1)] for i in range(n)]
        def helper(ind,w):
            if(dp[ind][w]!=-1):
                return(dp[ind][w])
            if(w==0):
                dp[ind][w]=0
                return(0)
            if(ind==0):
                if(wt[0]<=w):
                    dp[ind][w]=val[0]
                    return(val[0])
                else:
                    dp[ind][w]=0
                    return(0)
            take=-float("inf")
            notake=helper(ind-1,w)
            if(wt[ind]<=w):
                take=val[ind]+helper(ind-1,w-wt[ind])
            dp[ind][w]=max(take,notake)
            return(dp[ind][w])
        return(helper(n-1,W))
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends