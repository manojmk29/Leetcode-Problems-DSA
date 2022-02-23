class Solution(object):
    def titleToNumber(self, c):
        """
        :type columnTitle: str
        :rtype: int
        """
        ret=0
        m=1
        for i in c[::-1]:
            v=ord(i)-64
            ret+=(v*m)
            m*=26
        return(ret)