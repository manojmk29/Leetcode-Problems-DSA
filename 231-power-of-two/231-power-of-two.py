class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<1):
            return(False)
        n=abs(n)
        tot=int(math.log(n,2))
        while(tot):
            tot-=1
            if(n&1==1):
                return(False)
            n=n>>1
        return(True)
        