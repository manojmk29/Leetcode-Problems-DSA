class Solution:
    def sumSubarrayMins(self, arr):
        stk=[]
        n=len(arr)
        stk.append((arr[0],0))
        tot=arr[0]*len(arr)
        for i in range(1,len(arr)):
            last=i
            cnt=len(arr)-i
            while(stk and stk[-1][0]>arr[i]):
                val=stk.pop()
                tot+=(arr[i]-val[0])*(last-val[1])*cnt
                last=val[1]
            stk.append((arr[i],last))
            tot+=arr[i]*cnt
        return(tot%int(1e9+7))