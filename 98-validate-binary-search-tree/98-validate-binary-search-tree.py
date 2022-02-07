# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root,floor=-float("inf"),ceil=float("inf")):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(not root):
            return(True)
        if(root.val<=floor or root.val>=ceil):
            return(False)
        return(self.isValidBST(root.left,floor,root.val) and self.isValidBST(root.right,root.val,ceil))
    
        # if(not root):
        #     return(True)
        # left=self.isValidBST(root.left)
        # right=self.isValidBST(root.right)
        # if(not left or not right):
        #     return(False)
        # if(root.left and root.left.val>=root.val):
        #     return(False)
        # if(root.right and root.right.val<=root.val):
        #     return(False)
        # return(True)
            