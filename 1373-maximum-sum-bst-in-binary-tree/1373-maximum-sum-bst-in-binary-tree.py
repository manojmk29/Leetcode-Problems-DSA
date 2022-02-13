# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret=0
        def helper(root):
            if (not root):
                return(0,-float("inf"),float("inf"))    
            left=helper(root.left)
            right=helper(root.right)
            if(not left or not right or left[1]>=root.val or right[2]<=root.val):
                return(False)
            tot=root.val+left[0]+right[0]
            self.ret=max(self.ret,tot)
            return(tot,max(left[1],right[1],root.val),min(left[2],right[2],root.val))
        helper(root)
        return(self.ret)