class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)
        tot=sum(cardPoints)
        temp=0
        for i in range(n-k):
            temp+=cardPoints[i]
        l=0
        val=temp
        for i in range(n-k,n):
            val-=cardPoints[l]
            val+=cardPoints[i]
            l+=1
            temp=min(val,temp)
        return(tot-temp)