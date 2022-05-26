#User function Template for python3

class Solution:
    def minStep (self, n):
        #complete the function here
        step=0
        cur=n
        while(cur>1):
            if(cur%3==0):
                cur/=3
            else:
                cur-=1
            step+=1
        return(step)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minStep(n))
# } Driver Code Ends