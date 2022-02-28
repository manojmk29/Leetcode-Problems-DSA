class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap=collections.defaultdict(int)
        for i in s:
            hmap[i]+=1
        hset=set()
        ret=0
        for i in hmap:
            if hmap[i] not in hset:
                hset.add(hmap[i])
            else:
                k=hmap[i]
                while(k in hset):
                    k-=1
                    ret+=1
                if k!=0:
                    hset.add(k)
        return(ret)