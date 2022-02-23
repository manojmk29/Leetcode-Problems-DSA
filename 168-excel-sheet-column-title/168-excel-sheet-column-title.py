class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # return("A")
        ret=""
        inp=columnNumber
        while(inp):
            v=inp%26
            # if(inp==26):
            #     inp=0
            # else:
            inp//=26
            if(v==0):
                inp-=1
                ret="Z"+ret
            else:
                ret=chr(v+64)+ret
        return(ret)