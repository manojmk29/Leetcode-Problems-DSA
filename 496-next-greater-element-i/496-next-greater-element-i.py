class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #method 2
        hmap={}
        stack=[]
        n1=len(nums1)
        n2=len(nums2)
        for i in range(n2-1,-1,-1):
            val=nums2[i]
            while(stack and val>stack[-1]):
                stack.pop()
            if(stack):
                hmap[val]=stack[-1]
            else:
                hmap[val]=-1
            stack.append(val)
        ret=[]
        for i in nums1:
            if i not in hmap:
                ret.append(-1)
            else:
                ret.append(hmap[i])
        return(ret)
        
        #method 1
        #O(n*m)
        # for i in range(len(nums1)):
        #     x=nums1[i]
        #     flag=0
        #     maxi=-1
        #     for j in range(len(nums2)):
        #         if(nums2[j]==x):
        #             flag=1
        #         if(flag==1):
        #             if(nums2[j]>x):
        #                 maxi=nums2[j]
        #                 break
        #     nums1[i]=maxi    
        # return(nums1)