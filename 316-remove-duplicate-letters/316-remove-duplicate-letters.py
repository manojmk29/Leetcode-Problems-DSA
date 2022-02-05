class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        hmap={}
        for i in range(len(s)):
            if i not in hmap:
                hmap[s[i]]=i
            else:
                hmap[s[i]]=i
        ret=None
        stack=collections.deque()
        hset=set()
        for i in range(len(s)):
            if(s[i] not in hset):
                while(stack and stack[-1]>s[i] and hmap[stack[-1]]>i):
                    hset.remove(stack[-1])
                    stack.pop()
                hset.add(s[i])
                stack.append(s[i])
        string=""
        for i in stack:
            string+=i
        return(string)