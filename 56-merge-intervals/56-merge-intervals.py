class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret=[]
        l=intervals[0][0]
        r=intervals[0][1]
        for i in range(1,len(intervals)):
            if (intervals[i][0]<=r):
                r=max(r,intervals[i][1])
            else:
                ret.append([l,r])
                l=intervals[i][0]
                r=intervals[i][1]
        ret.append([l,r])
        return(ret)