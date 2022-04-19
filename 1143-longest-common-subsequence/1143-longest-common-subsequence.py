class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        prev=[0 for i in range(n+1)]
        cur=[0 for i in range(n+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(text1[i-1]==text2[j-1]):
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(prev[j],cur[j-1])
            prev=cur[:]
        return(prev[n])