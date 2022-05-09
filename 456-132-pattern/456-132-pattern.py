class Solution:
    def find132pattern(self,nums):
        stk=[]
        mint=nums[0]
        for i in nums[1:]:
            while(stk and stk[-1][0]<=i):
                stk.pop()
            if stk and stk[-1][0]>i and stk[-1][1]<i:
                return(True)
            stk.append([i,mint])
            mint=min(mint,i)
        return False