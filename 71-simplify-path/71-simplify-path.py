class Solution:
    def simplifyPath(self, path: str) -> str:
        stk=[]
        flag=0
        for i in path:
            if(i=="/"):
                if(flag==2):
                    f=0
                    for i in range(2):
                        if(stk[-1][i]!="."):
                            f=1
                    if(f==0):
                        stk.pop()
                        if(stk):
                            stk.pop()
                elif(flag==1):
                    if(stk[-1][0]=="."):
                        stk.pop()
                flag=0
            else:
                if(flag==0):
                    stk.append(i)
                    flag=1
                elif(flag>0):
                    val=stk.pop()
                    val+=i
                    flag+=1
                    stk.append(val)
        ret=""
        if(stk and stk[-1]=="."):
            stk.pop()
        if(stk and stk[-1]==".."):
            stk.pop()
            if(stk):
                stk.pop()
        for i in stk:
            ret+="/"
            ret+=i
        if(not ret):
            return("/")
        return(ret)