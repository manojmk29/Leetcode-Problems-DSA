class Solution:
    def minSpeedOnTime(self, dist, hour: float) -> int:
        def check(s):
            cur=0
            for i in range(len(dist)):
                cur=ceil(cur)
                val=dist[i]/s
                cur+=val
            if(cur>hour):
                return(False)
            return(True)
        l=1
        r=10000000
        pos=-1
        while(l<=r):
            mid=(l+r)//2
            if(check(mid)):
                pos=mid
                r=mid-1
            else:
                l=mid+1
        return(pos)