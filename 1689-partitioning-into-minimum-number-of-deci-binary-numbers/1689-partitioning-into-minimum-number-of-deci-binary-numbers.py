class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        t=1
        l=[int(i) for i in n]
        ret=0
        while(t==1):
            f=0
            for i in range(len(l)):
                if(l[i]>0):
                    f=1
                l[i]-=1
            if(f==0):
                return(ret)
            else:
                ret+=1
                    
                    
            
            