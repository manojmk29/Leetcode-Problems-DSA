class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        n=len(num)
        ret=[]
        for i in num:
            while(stack and stack[-1]>i and k):
                stack.pop()
                k-=1
            if stack or i!="0":
                stack.append(i)
        if k:
            stack=stack[0:-k]
        return("".join(stack) or "0")