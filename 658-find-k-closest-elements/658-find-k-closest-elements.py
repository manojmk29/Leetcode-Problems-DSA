class Solution:
    def findClosestElements(self, arr, k: int, x: int) :
        n=len(arr)
        d=k
        def findpos():
            n=len(arr)
            l=0
            r=n-1
            m=(l+r)//2
            while(l+1<r):
                m=(l+r)//2
                if(arr[m]==x):
                    return(m)
                elif(arr[m]>x):
                    r=m
                else:
                    l=m
            if(abs(arr[r]-x)<abs(arr[l]-x)):
                return(r)
            else:
                return(l)

        mid=findpos() 
        k-=1
        l=r=mid
        while(k):
            k-=1
            if(l==0):
                r+=1
            elif(r==n-1):
                l-=1
            else:
                if abs(x-arr[r+1])<abs(x-arr[l-1]):
                    r+=1
                else:
                    l-=1
        return(arr[l:l+d])  