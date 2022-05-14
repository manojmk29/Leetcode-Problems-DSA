from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        ret=0
        l=0
        hmap=defaultdict(int)
        for i in range(n):
            hmap[s[i]]+=1
            hn=len(hmap)
            if(hn==3):
                ret+=1
                val=n-i-1
                ret+=val
                while(len(hmap)==3):
                    hmap[s[l]]-=1
                    if(hmap[s[l]]==0):
                        hmap.pop(s[l])
                    else:
                        ret+=1
                        ret+=val
                    l+=1
        return(ret)