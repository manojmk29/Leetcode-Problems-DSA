class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hset=len(set(s))
        ret=0
        for i in range(1,hset+1):
            unique=0
            hmap=defaultdict(int)
            l=0
            sle=len(s)
            kk=set()
            for r in range(sle):
                val=s[r]
                hmap[val]+=1
                if(hmap[val]==1):
                    unique+=1
                if(hmap[val]==k):
                    kk.add(val)
                while(unique>i):
                    hmap[s[l]]-=1
                    if(hmap[s[l]]==0):
                        unique-=1
                    if(s[l] in kk and hmap[s[l]]<k):
                        kk.remove(s[l])
                    l+=1
                if(len(kk)==unique):
                    ret=max(ret,r-l+1)
        return(ret)        