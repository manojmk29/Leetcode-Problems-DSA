class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=list(s)
        vowel={"a","e","i","o","u","A","E","I","O","U"}
        i=0
        j=len(a)-1
        while(i<j):
            if(a[i] not in vowel):
                i+=1
            if(a[j] not in vowel):
                j-=1
            if(a[i] in vowel and a[j] in vowel):
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
        return("".join(a))
        # method 1
        
        # pos=[]
        # s=list(s)
        # vowel={"a","e","i","o","u","A","E","I","O","U"}
        # for i in range(len(s)):
        #     if s[i] in vowel:
        #         pos.append(i)
        # pos_len=len(pos)
        # for i in range(pos_len//2):
        #     s[pos[i]],s[pos[pos_len-1-i]]=s[pos[pos_len-1-i]],s[pos[i]]
        # return("".join(s))