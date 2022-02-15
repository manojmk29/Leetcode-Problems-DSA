class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxval=max(candies)
        ret=[]
        for i in candies:
            if((i+extraCandies)>=maxval):
                ret.append(True)
            else:
                ret.append(False)
        return(ret)