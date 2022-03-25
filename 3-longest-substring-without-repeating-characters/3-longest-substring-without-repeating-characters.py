class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(not s):
            return(0)
        ret=1
        cnt=0
        hset=set()
        left=0
        for i in range(0,len(s)):
            while(s[i] in hset):
                hset.remove(s[left])
                left+=1
            hset.add(s[i])
            ret=max(ret,i-left+1)
        return(ret)