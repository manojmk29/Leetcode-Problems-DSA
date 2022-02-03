class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxt=min(rectangles[0][0],rectangles[0][1])
        output=1
        for i in range(1,len(rectangles)):
            mint=min(rectangles[i][0],rectangles[i][1])
            if(mint>maxt):
                maxt=mint
                output=1
            elif(mint==maxt):
                output+=1
        return(output)