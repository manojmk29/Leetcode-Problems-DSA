class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        def merge(l,m,r):
            left=[arr[i] for i in range(l,m+1)]
            right=[arr[i] for i in range(m+1,r+1)]
            nl=len(left)
            nr=len(right)
            f=r-l+1
            ret=0
            temp=[]
            i=j=0
            while(i<nl and j<nr):
                if(right[j]<left[i]):
                    ret+=(nl-i)
                    temp.append(right[j])
                    j+=1
                else:
                    temp.append(left[i])
                    i+=1
            while(i<nl):
                temp.append(left[i])
                i+=1
            while(j<nr):
                temp.append(right[j])
                j+=1
            for i in range(f):
                arr[l+i]=temp[i]
            return(ret)
        def mergesort(l,r):
            ans=0
            if(l<r):
                m=(l+r)//2
                ans=0
                ans+=mergesort(l,m)
                ans+=mergesort(m+1,r)
                ans+=merge(l,m,r)
            return(ans)
        l=0
        r=n-1
        return(mergesort(l,r))

"""
2 4 1 3 5
1 2 3 4 5
"""
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends