#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    ret = []
	    def helper(ind,temp):
	        if ind==N:
	            ret.append(temp)
	            return
	        helper(ind+1,temp+arr[ind])
	        helper(ind+1,temp)
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