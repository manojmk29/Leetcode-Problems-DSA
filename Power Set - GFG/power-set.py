#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n=len(s)
		ret=[]
		for i in range(1,pow(2,n)):
		    temp=""
		    for j in range(n):
		        if(i&1<<j):
		            temp+=s[j]
		    ret.append(temp)
		return(sorted(ret))
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends