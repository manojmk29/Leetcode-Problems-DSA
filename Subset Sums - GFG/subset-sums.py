#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    ret=[]
	    n=len(arr)
	    def helper(ind,cur):
	        if(ind==n):
	            ret.append(cur)
	            return
	        helper(ind+1,cur)
	        helper(ind+1,cur+arr[ind])
	    helper(0,0)
	    return ret
	        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends