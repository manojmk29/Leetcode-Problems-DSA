class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        hmap={}
        def helper(word):
            if word in hmap:
                return(hmap[word])
            if(len(word)==0):
                hmap[word]=True
                return(True)
            for i in range(len(word),0,-1):
                if((word[0:i] in wordDict) and (helper(word[i:]) == True ) ):
                    hmap[word]=True
                    return(True)
            hmap[word]=False
            return(False)
        return(helper(s))
        