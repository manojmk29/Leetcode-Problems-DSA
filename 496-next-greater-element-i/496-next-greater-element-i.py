class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap={}
        stk=[]
        for i in range(len(nums2)-1,-1,-1):
            while(stk and stk[-1]<=nums2[i]):
                stk.pop()
            if(not stk):
                hmap[nums2[i]]=-1
            else:
                hmap[nums2[i]]=stk[-1]
            stk.append(nums2[i])
        ret=[]
        for i in nums1:
            ret.append(hmap[i])
        return(ret)
        