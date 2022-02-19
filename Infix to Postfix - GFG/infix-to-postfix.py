#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        def prec(v):
            if(v=="*" or v=="/"):
                return(2)
            elif(v=="+" or v=="-"):
                return(1)
            elif(v=="^"):
                return(3)
            else:
                return(0)
        hmap={}
        hmap["+"]=1
        hmap["-"]=1
        hmap["*"]=2
        hmap["/"]=2
        hmap["^"]=3
        ret=[]
        stk=[]
        for i in exp:
            if(i not in hmap):
                if(i=="("):
                    stk.append("(")
                elif(i==")"):
                    while(stk and stk[-1]!="("):
                        ret.append(stk.pop())
                    stk.pop()
                else:
                    ret.append(i)
            else:
                val=hmap[i]
                if(i=="^"):
                    if(not stk):
                        stk.append("^")
                    elif(stk and stk[-1]=="^"):
                        stk.append("^")
                    else:
                        while(stk and stk[-1]!="(" and hmap[stk[-1]]>=val):
                            ret.append(stk.pop())
                        stk.append(i)
                else:
                    while(stk and stk[-1]!="(" and hmap[stk[-1]]>=val):
                            ret.append(stk.pop())
                    stk.append(i)
        while(stk):
            ret.append(stk.pop())
        return("".join(ret))
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends