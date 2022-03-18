class Solution(object):
    def subarraysDivByK(self, nums, k):
        hmap={0:1}
        prev=0
        ret=0
        for i in nums:
            prev+=i
            prev%=k
            if(prev in hmap):
                ret+=hmap[prev]
                hmap[prev]+=1
            else:
                hmap[prev]=1
        return(ret)
        