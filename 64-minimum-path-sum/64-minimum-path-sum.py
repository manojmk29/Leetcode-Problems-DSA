class Solution(object):
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                up=(grid[i-1][j] if(i>0) else float("inf"))
                left=(grid[i][j-1] if(j>0) else float("inf"))
                ans=min(up,left)
                ans=ans if ans!=float("inf") else 0
                grid[i][j]+=ans
        return(grid[-1][-1]) 