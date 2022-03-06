class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hmap={}
        for i,j in enumerate(s):
            hmap[j]=i
        ret=[]
        l=r=None
        for ind,val in enumerate(s):
            if(l==None):
                l=ind
                r=hmap[val]
            if(ind==r):
                le=r-l+1
                ret.append(le)
                l=None
            elif(hmap[val]>r):
                r=hmap[val]
        return(ret)
                