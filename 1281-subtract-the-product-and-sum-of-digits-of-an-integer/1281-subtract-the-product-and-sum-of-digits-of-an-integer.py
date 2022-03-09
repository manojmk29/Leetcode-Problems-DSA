class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        f=str(n)
        prd=1
        for i in f:
            prd*=int(i)
        cnt=0
        for i in f:
            cnt+=int(i)
        return(prd-cnt)
        