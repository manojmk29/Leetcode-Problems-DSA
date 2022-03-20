class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        inp=[]
        rem=0
        m=len(num1)
        n=len(num2)
        while(m or n):
            if(not m):
                l=0
            else:
                l=ord(num1[m-1])%48
                m-=1
            if(not n):
                r=0
            else:
                r=ord(num2[n-1])%48
                n-=1
            tot=l+r+rem
            if(tot>=10):
                rem=tot//10
            else:
                rem=0
            val=tot%10
            inp.append(str(val))
        if(rem):
            inp.append(str(rem))
        return("".join(inp[::-1]))
            
            