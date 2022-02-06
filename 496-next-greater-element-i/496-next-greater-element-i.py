class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        #method 1
        
        for i in range(len(nums1)):
            x=nums1[i]
            flag=0
            maxi=-1
            for j in range(len(nums2)):
                if(nums2[j]==x):
                    flag=1
                if(flag==1):
                    if(nums2[j]>x):
                        maxi=nums2[j]
                        break
            nums1[i]=maxi    
        return(nums1)