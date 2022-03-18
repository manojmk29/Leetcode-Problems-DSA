class Solution(object):
    def maxArea(self, h, w, hc, vc):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        l=0
        left=0
        hc.sort()
        for i in hc:
            left=max(left,i-l)
            l=i
        left=max(h-l,left)
        r=0
        right=0
        vc.sort()
        for i in vc:
            right=max(right,i-r)
            r=i
        right=max(w-r,right)
        return((left*right)%(pow(10,9)+7))