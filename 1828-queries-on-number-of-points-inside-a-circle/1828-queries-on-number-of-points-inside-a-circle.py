class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ret=[]
        for i in queries:
            l=i[0]+i[2]
            r=i[1]+i[2]
            out=0
            for j in points:
                dist=sqrt(pow(i[0]-j[0],2)+pow(i[1]-j[1],2))
                if(dist<=i[2]):
                    out+=1
            ret.append(out)
        return(ret)
            