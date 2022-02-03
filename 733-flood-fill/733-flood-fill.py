class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        val=image[sr][sc]
        m=len(image)
        n=len(image[0])
        def rec(sr,sc):
            if(sr>=m or sr<0 or sc<0 or sc>=n or image[sr][sc]!=val) :
                return
            image[sr][sc]=newColor
            rec(sr-1,sc)
            rec(sr+1,sc)
            rec(sr,sc-1)
            rec(sr,sc+1)
        if(image[sr][sc]==newColor):
            return(image)
        rec(sr,sc)
        return(image)