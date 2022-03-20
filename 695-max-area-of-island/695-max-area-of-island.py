class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        def dfs(r,c):
            if(r<0 or r==m or c<0 or c==n or grid[r][c]==0):
                return(0)
            grid[r][c]=0
            return(1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1))
        ret=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    ret=max(ret,dfs(i,j))
        return(ret)