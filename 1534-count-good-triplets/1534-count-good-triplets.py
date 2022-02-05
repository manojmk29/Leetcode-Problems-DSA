class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        l=len(arr)
        res=0
        for i in range(0,l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                    if(abs(arr[i]-arr[j])<=a):
                        if(abs(arr[k]-arr[j])<=b):
                            if(abs(arr[i]-arr[k])<=c):
                                res+=1
        return(res)
                                