class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sw=[]
        tw=[]
        for i in s:
            if i!="#":
                sw.append(i)
            elif sw:
                sw.pop()
        for i in t:
            if i!="#":
                tw.append(i)
            elif tw:
                tw.pop()
        return(tw==sw)
            