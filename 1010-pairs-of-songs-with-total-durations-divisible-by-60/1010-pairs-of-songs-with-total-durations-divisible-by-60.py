class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        hmap=defaultdict(int)
        val=time[0]%60
        val=val if(val>0) else 60
        hmap[val]=1
        ret=0
        for i in range(1,len(time)):
            val=time[i]%60
            ret+=hmap[60-val]
            val=val if(val>0) else 60
            hmap[val]+=1
        return(ret)