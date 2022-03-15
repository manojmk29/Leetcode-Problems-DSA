class Solution(object):
    def decodeString(self, s):
        stk=[]
        num=0
        curr=""
        for i in s:
            if(i=="["):
                stk.append(curr)
                stk.append(num)
                curr=""
                num=0
            elif(i=="]"):
                n=stk.pop()
                prev=stk.pop()
                tt=n*curr
                curr=prev+tt
            elif(i.isdigit()):
                num=num*10+int(i)
            else:
                curr+=i
        return(curr)