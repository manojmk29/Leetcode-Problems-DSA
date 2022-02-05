class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	  hset=set()
    	  ret=set()
    	  for i in arr:
    	      if i in hset:
    	          if(i not in ret):
    	            ret.add(i)
    	      else:
    	          hset.add(i)
    	  if(len(ret)==0):
    	      return([-1])
    	  return(sorted(ret))

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends