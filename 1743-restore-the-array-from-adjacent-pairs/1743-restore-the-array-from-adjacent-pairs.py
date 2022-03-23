class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        hmap=defaultdict(set)
        for i in adjacentPairs:
            hmap[i[0]].add(i[1])
            hmap[i[1]].add(i[0])
        for i in hmap:
            if(len(hmap[i])==1):
                start=i
                break
        def dfs(start):
            ret.append(start)
            for i in hmap[start]:
                hmap[i].remove(start)
                dfs(i)
        ret=[]
        dfs(start)
        return(ret)
            
            