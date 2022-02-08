class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        n=len(height)
        r=n-1
        ret=0
        while(l<r):
            dist=r-l
            val=min(height[r],height[l])
            ret=max(ret,val*dist)
            if(val==height[l]):
                l+=1
            else:
                r-=1
        return(ret)