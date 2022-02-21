class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=1
        for i in range(1,n):
            l,r=r,l+r
        return(r)
        