#User function Template for python3

class Solution:
    def solve(self, arr, n):
        # code here
        arr.sort()
        a=b=""
        f=-1
        for i in arr:
            if(f==-1):
                a+=str(i)
            else:
                b+=str(i)
            f*=-1
        return((int(a) if a else 0)+ (int(b) if b else 0))
        
        
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