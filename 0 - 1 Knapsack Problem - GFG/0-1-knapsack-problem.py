#User function Template for python3
class Solution:
    def knapSack(self,W, wt, val, n):
        dp=[0 for i in range(W+1)]
        for i in range(wt[0],W+1):
            dp[i]=val[0]
        for ind in range(1,n):
            next=[0 for i in range(W+1)]
            for weit in range(0,W+1):
                notTaken =dp[weit];
                taken = -float("inf");
                if(wt[ind] <= weit):
                    taken = val[ind] + dp[weit - wt[ind]]
                next[weit] = max(notTaken, taken)
            dp=next
        return(dp[W])
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