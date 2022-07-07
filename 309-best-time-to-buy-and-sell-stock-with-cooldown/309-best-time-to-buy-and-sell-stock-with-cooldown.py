class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        inh=-prices[0]
        nos=0
        sold=0
        for i in range(1,n):
            n_inh=max(inh,nos-prices[i])
            n_nos=max(nos,sold)
            n_sold=max(sold,inh+prices[i])
            inh,nos,sold=n_inh,n_nos,n_sold
        return(max(nos,sold))

                    
            