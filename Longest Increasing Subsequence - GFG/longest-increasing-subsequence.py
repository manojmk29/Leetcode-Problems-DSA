#User function Template for python3
from functools import lru_cache
class Solution:
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,arr,n):
        @lru_cache(maxsize=1000)
        def helper(ind,l):
            ret=l
            for i in range(ind+1,n):
                if(arr[i]>arr[ind]):
                    ret=max(ret,helper(i,l+1))
            return(ret)
        t=1
        for i in range(n):
            t=max(t,helper(i,1))
        return(t)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends