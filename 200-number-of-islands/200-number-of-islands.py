class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r=len(grid)
        c=len(grid[0])
        ret=0
        def helper(k,l):
            if(k>=r or k<0 or l>=c or l<0):
                return
            if(grid[k][l]=="-1" or grid[k][l]=="0"):
                return
            else:
                grid[k][l]="-1"
                helper(k+1,l)
                helper(k-1,l)
                helper(k,l-1)
                helper(k,l+1)
        for i in range(r):
            for j in range(c):
                if(grid[i][j]=="1"):
                    ret+=1
                    helper(i,j)
        return(ret)