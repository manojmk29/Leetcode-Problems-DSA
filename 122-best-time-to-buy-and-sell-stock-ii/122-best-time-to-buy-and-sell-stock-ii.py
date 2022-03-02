class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=r=0
        n=len(prices)
        ret=0
        for i in range(1,n+1):
            if(i<n):
                val=prices[i]
                if(val<prices[r]):
                    ret+=(prices[r]-prices[l])
                    l=r=i
                else:
                    r=i
            else:
                ret+=(prices[r]-prices[l])
        return(ret)
        
                