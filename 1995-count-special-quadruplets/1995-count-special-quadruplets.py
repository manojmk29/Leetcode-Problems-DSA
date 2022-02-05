class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap=defaultdict(lambda:0)
        hmap[nums[-1]-nums[-2]]=1
        res=0
        n=len(nums)
        for b in range(n-3,0,-1):
            for a in range(b-1,-1,-1):
                res+=hmap[nums[a]+nums[b]]
            for d in range(n-1,b-1,-1):
                hmap[nums[d]-nums[b]]+=1
        return(res)
                
        