class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd=set(wordDict)
        mem={}
        def helper(pos):
            if(pos==len(s)):
                return(True)
            if pos in mem:
                return(mem[pos])
            for i in range(pos,len(s)):
                if(s[pos:i+1] in wd and helper(i+1)):
                    mem[pos]=True
                    return(True)
            mem[pos]=False
            return(False)
        return(helper(0))