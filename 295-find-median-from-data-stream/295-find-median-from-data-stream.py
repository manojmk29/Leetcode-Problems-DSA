from heapq import *
class MedianFinder(object):
    def __init__(self):
        self.first=[]
        self.second=[]
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        fn=len(self.first)
        sn=len(self.second)
        if(fn==sn):
            val=heappushpop(self.first,-num)
            heappush(self.second,-val)
        else:
            val=heappushpop(self.second,num)
            heappush(self.first,-val)
            
    def findMedian(self):
        """
        :rtype: float
        """
        fn=len(self.first)
        sn=len(self.second)
        if(fn==sn):
            return(self.second[0]-self.first[0])/2.0
        else:
            return(self.second[0])
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()