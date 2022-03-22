class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1=m2=m3=float("inf")
        l1=l2=l3=-float("inf")
        for i in nums:
            if(i<m1):
                m2,m3=m3,m2
                m1,m2=m2,m1
                m1=i
            elif(i<m2):
                m2,m3=m3,m2
                m2=i
            elif(i<m3):
                m3=i
            if(i>l1):
                l2,l3=l3,l2
                l1,l2=l2,l1
                l1=i
            elif(i>l2):
                l2,l3=l3,l2
                l2=i
            elif(i>l3):
                l3=i
        return max(l1*l2*l3,m1*m2*l1)