class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        ret=0
        lastIntervalEnd=intervals[0][1]
        intervals=intervals[1:]
        for interval in intervals:
            if lastIntervalEnd > interval[0]:
                lastIntervalEnd = min(lastIntervalEnd, interval[1])
                ret+=1
            else:
                lastIntervalEnd = interval[1]   
        return(ret)
                
#         for i in range(1,len(intervals)):
#             if((intervals[i][0]==l) or (intervals[i][0]<r)):
#                 ret+=1
#                 r=min(r,intervals[i][1])
#             # elif(intervals[i][0]<r):
#             #     r=min(r,intervals[i][1])
#             #     ret+=1
#         return(ret)
    