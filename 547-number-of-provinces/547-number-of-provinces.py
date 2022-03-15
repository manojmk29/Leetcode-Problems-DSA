class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        flag=[0]*n
        def helper(ind):
            if(flag[ind]!=-1):
                flag[ind]=-1
                for i in range(n):
                    if(isConnected[ind][i]==1):
                        helper(i)
        ret=0
        for i in range(n):
            if(flag[i]==0):
                ret+=1
                helper(i)
        return(ret)