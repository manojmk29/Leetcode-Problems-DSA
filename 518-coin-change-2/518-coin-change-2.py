"""
Here we are using memo technique.

"""
class Solution:
    def change(self, amount: int, coins) -> int:
        n=len(coins)
        dp=[[0 for i in range(amount+1)]for _ in range(n)]
        for i in range(0,amount+1):
            if(i%coins[0]==0):
                dp[0][i]=1
            else:
                dp[0][i]=0
        for ind in range(1,len(coins)):
            for val in range(0,amount+1):
                notake=dp[ind-1][val]
                take=0
                if(coins[ind]<=val):
                    take=dp[ind][val-coins[ind]]
                dp[ind][val]=take+notake
        val=dp[n-1][amount]
        return(val)