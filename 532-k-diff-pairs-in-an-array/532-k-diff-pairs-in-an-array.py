class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hset=set()
        rset=set()
        ret=0
        for i in nums:
            if i-k in hset and i-k not in rset:
                ret+=1
                rset.add(i-k)
            if i+k in hset and i not in rset:
                ret+=1
                rset.add(i)
            hset.add(i)
        return(ret)