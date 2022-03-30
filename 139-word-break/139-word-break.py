class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict=set(wordDict)
        @lru_cache
        def helper(word):
            if(len(word)==0):
                return(True)
            for i in range(len(word),0,-1):
                if((word[0:i] in wordDict) and (helper(word[i:]) == True ) ):
                    return(True)
            return(False)
        return(helper(s))
        