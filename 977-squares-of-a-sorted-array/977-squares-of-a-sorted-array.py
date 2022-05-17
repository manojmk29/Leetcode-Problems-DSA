class Solution:
    def sortedSquares(self, arr):
        n=br=len(arr)
        for i in range(len(arr)):
            if(br==len(arr) and arr[i]>=0):
                br=i
            arr[i]=arr[i]*arr[i]
        pos=[]
        neg=[]
        ret=[]
        for i in range(br,n):
            pos.append(arr[i])
        for i in range(br):
            neg.append(arr[i])
        neg=neg[::-1]
        nn=len(neg)
        np=len(pos)
        i=j=0
        while(i<nn and j<np):
            if(neg[i]>pos[j]):
                ret.append(pos[j])
                j+=1
            else:
                ret.append(neg[i])
                i+=1
        while(i<nn):
            ret.append(neg[i])
            i+=1
        while(j<np):
            ret.append(pos[j])
            j+=1
        return(ret)
            