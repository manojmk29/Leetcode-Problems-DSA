class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        mem=[-1 for i in range(n)]
        def helper(pos):
            if(pos>=n):
                return(0)
            if(mem[pos]!=-1):
                return mem[pos]
            val=0
            for i in range(pos+1,n):
                if(prices[i]>prices[pos]):
                    val=max(val,prices[i]-prices[pos]+helper(i+2))
            ret=max(helper(pos+1),val)
            mem[pos]=ret
            return(ret)
        return(helper(0))
                    
            