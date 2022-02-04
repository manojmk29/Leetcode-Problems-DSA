class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        # method 1
        pos=[]
        s=list(s)
        vowel={"a","e","i","o","u","A","E","I","O","U"}
        for i in range(len(s)):
            if s[i] in vowel:
                pos.append(i)
        pos_len=len(pos)
        for i in range(pos_len//2):
            s[pos[i]],s[pos[pos_len-1-i]]=s[pos[pos_len-1-i]],s[pos[i]]
        return("".join(s))