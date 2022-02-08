class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        a=n
        while(a):
            a&=a-1
            cnt+=1
        return(cnt)
        # return list(str(bin(n))).count('1')
        # a=int(str(n),2)
        
        # a=n
        # c=0
        # if(a==0):
        #     nn=0
        # else:
        #     nn=int(log(n,2))+1
        # while(nn):
        #     if(a&1==1):
        #         c+=1
        #     a=a>>1
        #     nn-=1
        # return(c)