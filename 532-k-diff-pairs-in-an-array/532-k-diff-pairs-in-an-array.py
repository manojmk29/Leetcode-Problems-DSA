class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hset=collections.Counter(nums)
        ret=0
        for i in hset:
            if (k>0 and i+k in hset) or (k==0 and hset[i]>1):
                ret+=1
        return(ret)