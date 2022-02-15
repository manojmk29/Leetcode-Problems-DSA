class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        hmap=defaultdict(int)
        ret=0
        for i in range(n):
            ret+=hmap[nums[i]]
            hmap[nums[i]]+=1
        return(ret)
            