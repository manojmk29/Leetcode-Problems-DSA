class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret=max(heights[0],heights[-1])
        hmap={}
        n=len(heights)
        for i in range(0,n):
            value=heights[i]
            if((value in hmap) and (i<=hmap[value])):
                continue
            l=r=i
            while(l>0 and heights[l-1]>=heights[i]):
                l-=1
            if(l==-1):
                l=0
            while(r<n-1 and heights[r+1]>=heights[i]):
                r+=1
            if(r==n):
                r=n-1
            hmap[value]=r
            val=(r-l+1)*heights[i]
            ret=max(val,ret)
        return(ret)