# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums,l=0,r=float("inf")):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if(r<l):
            return(None)
        if(r==float("inf")):
            r=len(nums)-1
        mid=(l+r)//2
        node=TreeNode(nums[mid])
        node.left=self.sortedArrayToBST(nums,l,mid-1)
        node.right=self.sortedArrayToBST(nums,mid+1,r)
        return(node)