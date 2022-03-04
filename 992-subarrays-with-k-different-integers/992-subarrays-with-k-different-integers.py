class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def helper(k):
            l=r=cnt=ret=0
            hmap=defaultdict(int)
            n=len(nums)
            while(r<n):
                hmap[nums[r]]+=1
                if(hmap[nums[r]]==1):
                    cnt+=1
                r+=1
                while(l<r and cnt>k):
                    hmap[nums[l]]-=1
                    if(hmap[nums[l]]==0):
                        cnt-=1
                    l+=1
                ret+=r-l
            return(ret)
        return(helper(k)-helper(k-1))