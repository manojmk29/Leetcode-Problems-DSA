class Solution:
	def editDistance(self, s, t):
		# Code here
		dp=[[0 for i in range(len(t)+1)] for i in range(len(s)+1)]
		r=0
		j=0
		for i in range(len(dp[0])):
		    dp[r][i]=j
		    j+=1
		j=0
		for i in range(len(dp)):
		    dp[i][r]=j
		    j+=1
		for i in range(1,len(s)+1):
		    for j in range(1,len(t)+1):
    		    if(s[i-1]==t[j-1]):
    		        dp[i][j]=dp[i-1][j-1]
    		    else:
    		        dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
		return(dp[len(s)][len(t)])
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends