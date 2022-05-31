class Solution:
    def maxDistance(self, position, m):
        ll=len(position)
        def check(val):
            n=1
            cur=position[0]
            for i in range(1,ll):
                if((position[i]-cur) >= val):
                    n+=1
                    cur=position[i]
                if(n==m):
                    return(True)
            return(False)
        mint=min(position)    
        maxt=max(position)
        diff=maxt-mint
        position.sort()
        l=0
        r=diff
        pos=0
        while(l<=r):
            mid=(l+r)//2
            if(check(mid)):
                l=mid+1
                pos=mid
            else:
                r=mid-1
        return(pos)