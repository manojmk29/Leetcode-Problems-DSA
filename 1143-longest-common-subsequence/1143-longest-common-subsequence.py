class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=[[0 for i in range(n)]for i in range(m)]
        dp[0][0]=int(text2[0]==text1[0])
        for i in range(1,m):
            if(text2[0]==text1[i]):
                dp[i][0]=1
            else:
                dp[i][0]=dp[i-1][0]
        for i in range(1,n):
            if(text1[0]==text2[i]):
                dp[0][i]=1
            else:
                dp[0][i]=dp[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                if(text1[i]==text2[j]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return(dp[m-1][n-1])