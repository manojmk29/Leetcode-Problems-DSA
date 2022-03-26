class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=digits[::-1]
        carry=1
        for i in range(len(digits)):
            val=digits[i]+carry
            digits[i]=val%10
            carry=val//10
        if(carry):
            digits.append(carry)
        return(digits[::-1])