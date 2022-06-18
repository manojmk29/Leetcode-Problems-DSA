class Solution:
    def climbStairs(self, n: int) -> int:
        dp=collections.defaultdict(int)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]+=dp[i-2]
            dp[i]+=dp[i-1]
        return(dp[n])
        