import collections
class Solution(object):
    def findOrder(self,numCourses,prerequisites):
        hmap=collections.defaultdict(list) 
        for i in prerequisites: 
            hmap[i[1]].append(i[0]) 
        flag=[0 for i in range(numCourses)]
        def check(ind):
            if(flag[ind]==-1):
                return(False)
            flag[ind]=-1
            for i in hmap[ind]:
                if(not check(i)):
                    return(False)
            flag[ind]=0
            return(True)
        for i in range(numCourses):
            if(not check(i)):
                return([])
        stk=[]
        def helper(ind):
            if(flag[ind]==0):
                flag[ind]=-1
                for i in hmap[ind]:
                    helper(i)
                stk.append(ind)
        for i in range(numCourses):
            helper(i)
        return(stk[::-1])