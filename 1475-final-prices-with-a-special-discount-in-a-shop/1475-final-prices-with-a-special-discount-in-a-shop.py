class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ret=prices
        stack=[]
        stack.append((prices[0],0))
        for i in range(1,len(prices)):
            while(stack and stack[-1][0]>=prices[i]):
                val=stack.pop()
                ret[val[1]]=ret[val[1]]-prices[i]
            stack.append((prices[i],i))
        return(ret)
    