class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hmap1={}
        for i in nums1:
            for j in nums2:
                if(i+j not in hmap1):
                    hmap1[i+j]=1
                else:
                    hmap1[i+j]+=1
        hmap2={}
        for i in nums3:
            for j in nums4:
                if(i+j not in hmap2):
                    hmap2[i+j]=1
                else:
                    hmap2[i+j]+=1
        out=0
        for i in hmap1:
            if (-i in hmap2):
                out+=(hmap1[i]*hmap2[-i])
        return(out)
                    
                