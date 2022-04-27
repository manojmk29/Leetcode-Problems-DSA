class Solution:
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        def dfs(inp):
            if(flag[inp]==1):
                return
            flag[inp]=1
            arr.append(inp)
            for i in val[inp]:
                dfs(i)
        import collections
        val=collections.defaultdict(list)
        s=list(s)
        for i in pairs:
            val[i[0]].append(i[1])
            val[i[1]].append(i[0])
        flag=[0 for i in range(len(s))]
        for i in val:
            arr=[]
            dfs(i)
            if(arr):
                arr=sorted(arr)
                mod=[s[i] for i in arr]
                mod.sort()
                for i in range(len(arr)):
                    s[arr[i]]=mod[i]
        return(''.join(s))