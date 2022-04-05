class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1 for i in range(amount+1)]for _ in range(len(coins))]
        def helper(ind,tot):
            if(ind==0):
                if(tot%coins[0]==0):
                    return(tot//coins[0])
                else:
                    return(float("inf"))
            if(dp[ind][tot]!=-1):
                return(dp[ind][tot])
            notake=helper(ind-1,tot)
            take=float("inf")
            if(coins[ind]<=tot):
                take=1+helper(ind,tot-coins[ind])
            ret=min(notake,take)
            dp[ind][tot]=ret
            return(ret)
        val=helper(len(coins)-1,amount)
        return(val if val!=float("inf") else -1)