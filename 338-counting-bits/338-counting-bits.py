class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret=[0 for i in range(n+1)]
        if(not n):
            return(ret)
        ret[1]=1
        for i in range(2,n+1):
            if(i&1==1):
                ret[i]=ret[i//2]+1
            else:
                ret[i]=ret[i//2]
        return(ret)
            