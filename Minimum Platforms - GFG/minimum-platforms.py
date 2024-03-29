#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
    	dep.sort()
    	i=0
    	j=0
    	ret=1
    	cnt=0
    	while(i<len(arr)):
    	    if(arr[i]<=dep[j]):
    	        i+=1
    	        cnt+=1
    	    else:
    	        j+=1
    	        cnt-=1
    	    ret=max(ret,cnt)
    	return(ret)
    	#0900, 0940, 0950, 1100, 1500, 1800
    	#0910, 1120, 1130,1200, 1900, 2000
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends