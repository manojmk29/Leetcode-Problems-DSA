#User function Template for python3

def minSwap (arr, n, k) : 
    #Complete the function
    temp=[0]
    cur=0
    for i in arr:
        if i <=k:
            cur+=1
        temp.append(cur)
    end=n-cur
    ret=cur
    for i in range(end+1):
        val=temp[i+cur]-temp[i]
        val=cur-val
        ret=min(ret,val)
    return(ret)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends