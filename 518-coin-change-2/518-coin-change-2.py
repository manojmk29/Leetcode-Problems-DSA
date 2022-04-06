"""
Here we are using memo technique.

"""
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins) -> int:
        dp=[[-1 for i in range(amount+1)]for _ in range(len(coins))]
        @lru_cache(None)
        def helper(ind,tot):
            if(ind==0):
                if(tot%coins[0]==0):
                    return(1)
                else:
                    return(0)
            if(dp[ind][tot]!=-1):
                return(dp[ind][tot])
            notake=helper(ind-1,tot)
            take=0
            if(coins[ind]<=tot):
                take=helper(ind,tot-coins[ind])
            ret=notake+take
            dp[ind][tot]=ret
            return(ret)
        val=helper(len(coins)-1,amount)
        return(val)