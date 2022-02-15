class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        n=len(nums)
        self.nums=nums
        heapify(nums)
        self.k=k
        while(n>k):
            heappop(self.nums)
            n-=1
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if(len(self.nums)<self.k):
            heappush(self.nums,val)
        elif(val>self.nums[0]):
            heappop(self.nums)
            heappush(self.nums,val)
        return(self.nums[0])
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)