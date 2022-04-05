class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1 for i in range(amount+1)]
        dp[0]=0
        def helper(tot):
            if(dp[tot]!=-1):
                return(dp[tot])
            if(tot==0):
                return(0)
            if(tot<0):
                return(float("inf"))
            ret=float("inf")
            for i in coins:
                if(i<=tot):
                    ret=min(ret,1+helper(tot-i))
            dp[tot]=ret
            return(ret)
        val=helper(amount)
        return(val if val!=float("inf") else -1)