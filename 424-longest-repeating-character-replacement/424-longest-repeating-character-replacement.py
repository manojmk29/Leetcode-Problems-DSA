class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hmap=collections.defaultdict(int)
        start=0
        n=len(s)
        mct=0
        maxt=0
        for end,j in enumerate(s):
            hmap[j]+=1
            mct=max(hmap[j],mct)
            while(end-start+1-mct>k):
                hmap[s[start]]-=1
                start+=1
            l=end-start+1
            maxt=max(l,maxt)
        return(maxt)