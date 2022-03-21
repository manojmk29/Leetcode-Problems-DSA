class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hmap={}
        ret=[]
        for i in range(len(s)):
            hmap[s[i]]=i
        last=-1
        prev=0
        for i in range(len(s)):
            last=max(last,hmap[s[i]])
            if(last==i):
                ret.append(i+1-prev)
                prev=i+1
                last=-1
        return(ret)
            