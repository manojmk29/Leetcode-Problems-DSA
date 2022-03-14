class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret=[0]
        ptr=0
        flag=2
        for i in range(n):
            val=ret[ptr]
            if(flag==1):
                ret.append(val)
                flag+=1
            elif(flag==2 or flag==3):
                ret.append(val+1)
                flag+=1
            elif(flag==4):
                ret.append(val+2)
                ptr+=1
                flag=1
        return(ret)