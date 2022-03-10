#User function Template for python3

class Solution:
    def solve(self, arr, n):
        # code here
        arr.sort()
        a=0
        b=0
        f=1
        for i in arr:
            if(f==1):
                a*=10
                a+=i
            else:
                b*=10
                b+=i
            f*=-1
        return(a+b)
        
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends