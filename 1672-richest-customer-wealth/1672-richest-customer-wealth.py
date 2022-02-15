class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        r=len(accounts)
        c=len(accounts[0])
        ret=0
        for i in range(r):
            w=0
            for j in range(c):
                w+=accounts[i][j]
            ret=max(ret,w)
        return(ret)
            