class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        hmap=collections.defaultdict(list)
        mint=float("inf")
        for i in range(1,len(arr)):
            dif=arr[i]-arr[i-1]
            hmap[dif].append([arr[i-1],arr[i]])
            mint=min(mint,dif)
        return(hmap[mint])
            
            
        