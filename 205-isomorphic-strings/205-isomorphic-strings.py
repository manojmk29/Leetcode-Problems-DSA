class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap={}
        hset=set()
        n=len(s)
        for i in range(n):
            if s[i] not in hmap:
                if(t[i] not in hset):
                    hmap[s[i]]=t[i]
                    hset.add(t[i])
                else:
                    return(False)
            else:
                if(hmap[s[i]]!=t[i]):
                    return(False)
        return(True)
        