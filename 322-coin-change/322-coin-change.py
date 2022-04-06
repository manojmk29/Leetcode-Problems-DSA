"""
Here we are using memo technique.

"""
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n=len(coins)
        dp=[[0 for i in range(amount+1)]for _ in range(n)]
        for i in range(1,amount+1):
            if(i%coins[0]==0):
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=float("inf")
        for ind in range(1,len(coins)):
            for val in range(1,amount+1):
                notake=dp[ind-1][val]
                take=float("inf")
                if(coins[ind]<=val):
                    take=1+dp[ind][val-coins[ind]]
                dp[ind][val]=min(take,notake)
        val=dp[n-1][amount]
        return(val if val!=float("inf") else -1)