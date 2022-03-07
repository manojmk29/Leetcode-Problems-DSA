class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        le=len(s)
        def helper(b,e):
            if(b<0 or e>=le):
                return(0)
            hmap=collections.defaultdict(int)
            se={}
            for i in range(b,e+1):
                hmap[s[i]]+=1
                if s[i] not in se:
                    se[s[i]]=[i,i]
                else:
                    se[s[i]][1]=i
            l=float("inf")
            r=-l
            for i in hmap:
                if(hmap[i]<k):
                    l=min(l,se[i][0])
                    r=max(r,se[i][1])
            if(l==float("inf")):
                return(e-b+1)
            else:
                return(max(helper(b,l-1),helper(l+1,e)))
        return(helper(0,le-1))