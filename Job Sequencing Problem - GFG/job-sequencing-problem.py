#User function Template for python3
import heapq
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
        arr=[]
        n=len(jobs)
        for i in range(n):
            v=(jobs[i].id,jobs[i].deadline,jobs[i].profit)
            arr.append(v)
        jobs=arr
        jobs.sort(key=lambda x:x[1])
        last=0
        hq=[]
        heapq.heapify(hq)
        for i in  jobs:
            dl=i[1]
            pr=i[2]
            if(dl!=last or len(hq)!=last):
                last=dl
                heapq.heappush(hq,pr)
            else:
                if(hq[0]<pr):
                    heapq.heapreplace(hq,pr)
        return(len(hq),sum(hq))
            # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends