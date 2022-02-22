class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[-1 for _ in range(n)]for _ in range(m)]
        dp[m-1][n-1]=0
        for i in range(m):
            dp[i][n-1]=1
        for i in range(n):
            dp[m-1][i]=1
        def helper(r,c):
            if(dp[r][c]!=-1):
                return(dp[r][c])
            else:
                dp[r][c]=helper(r+1,c)+helper(r,c+1)
            return(dp[r][c])
        return(helper(0,0))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        hmap={}
        def helper(i,j):
            if(i==m-1 and j==n-1):
                return(1)
            elif(i>=m or j>=n):
                return(0)
            if((i,j) in hmap):
                return(hmap[(i,j)])
            else:
                hmap[(i,j)]=helper(i+1,j)+helper(i,j+1)
                return(hmap[(i,j)])
        return(helper(0,0))