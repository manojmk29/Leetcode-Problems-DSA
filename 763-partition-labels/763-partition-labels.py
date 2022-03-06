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
        l=r=0
        for ind,val in enumerate(s):
            r=max(r,hmap[val])
            if(ind==r):
                le=r-l+1
                ret.append(le)
                l=r+1
        return(ret)
                