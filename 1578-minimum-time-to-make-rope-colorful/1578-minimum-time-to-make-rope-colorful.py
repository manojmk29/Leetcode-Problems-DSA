class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        prev=0
        ret=0
        n=len(colors)
        for i in range(1,n):
            if(colors[prev]==colors[i]):
                if(neededTime[prev]<neededTime[i]):
                    ret+=neededTime[prev]
                    prev=i
                else:
                    ret+=neededTime[i]
            else:
                prev=i
        return(ret)        