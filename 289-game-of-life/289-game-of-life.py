class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        flag=[[0 for i in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                cnt=0
                for x in(-1,0,1):
                    for y in(-1,-0,1):
                        if((0<=i+x<=m-1) and (0<=j+y<=n-1)):
                            cnt+=board[i+x][j+y] 
                cnt-=board[i][j]
                flag[i][j]=cnt
        for i in range(m):
            for j in range(n):
                val=board[i][j]
                if(val==1):
                    if(flag[i][j]<2):
                        board[i][j]=0
                    elif(flag[i][j]>3):
                        board[i][j]=0
                elif(flag[i][j]==3):
                    board[i][j]=1
            