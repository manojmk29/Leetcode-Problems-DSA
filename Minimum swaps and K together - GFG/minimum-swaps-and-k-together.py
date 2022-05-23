#User function Template for python3

def minSwap (arr, n, k) : 
    #Complete the function
    cur=0
    for i in arr:
        if i <=k:
            cur+=1
    ret=cur
    temp=0
    l=0
    for i in range(cur):
        if arr[i] <=k:
            temp+=1
    val=cur-temp
    ret=min(ret,val)
    for i in range(cur,n):
        if(arr[l]<=k):
            temp-=1
        l+=1
        if(arr[i]<=k):
            temp+=1
        val=cur-temp
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