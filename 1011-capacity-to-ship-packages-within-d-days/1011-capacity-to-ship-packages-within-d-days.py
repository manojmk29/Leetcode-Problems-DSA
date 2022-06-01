class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n=len(weights)
        def check(w):
            d=1
            cur=0
            for i in range(n):
                if(weights[i]>w):
                    return(False)
                if((cur+weights[i]) > w):
                    d+=1
                    cur=weights[i]
                else:
                    cur+=weights[i]
            if d>days:
                return False
            return(True)
        l=1
        r=ret=sum(weights)
        while(l<=r):
            mid=(l+r)//2
            if(check(mid)):
                ret=mid
                r=mid-1
            else:
                l=mid+1
        return(ret)