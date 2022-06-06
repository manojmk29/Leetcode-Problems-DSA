class Solution:
    def minimizedMaximum(self, n, q) -> int:
        lent=len(q)
        def check(val):
            cnt=0
            for i in range(lent):
                cnt+=ceil(q[i]/val)
            return(cnt)
        l=1
        r=max(q)
        while(l<r):
            mid=(l+r)//2
            c=check(mid)
            if(c>n):
                l=mid+1
            else:
                r=mid
        return(l)       