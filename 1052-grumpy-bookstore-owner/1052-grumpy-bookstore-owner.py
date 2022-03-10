class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        le=len(customers)
        tot=0
        for i in range(le):
            if(not grumpy[i]):
                tot+=customers[i]
        ret=tot
        l=0
        for i in range(minutes):
            if(grumpy[i]):
                tot+=customers[i]
        ret=max(ret,tot)
        for i in range(minutes,le):
            if(grumpy[l]):
                tot-=customers[l]
            l+=1
            if(grumpy[i]):
                tot+=customers[i]
            ret=max(ret,tot)
        return(ret)