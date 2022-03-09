class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        le=len(word)
        rl=len(board)
        cl=len(board[0])
        def helper(ind,r,c):
            if(ind>=le):
                return(True)
            if(r<0 or r>=rl or c<0 or c>=cl or board[r][c]!=word[ind]):
                return(False)
            tmp=board[r][c]
            board[r][c]="#"
            if(ind==le-1):
                return(True)
            for i in (1,-1):
                if(helper(ind+1,r,c+i) or helper(ind+1,r+i,c)):
                    return(True)
            board[r][c]=tmp
            return(False)
        for i in range(rl):
            for j in range(cl):
                if(helper(0,i,j)==True):
                    return(True)
        return(False)