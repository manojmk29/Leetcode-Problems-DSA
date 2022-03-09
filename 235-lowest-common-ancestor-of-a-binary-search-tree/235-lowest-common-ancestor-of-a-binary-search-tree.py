# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(root):
            if(not root):
                return(False)
            if(root==p or root==q):
                return(root)
            l=helper(root.left)
            r=helper(root.right)
            if(l and r):
                return(root)
            else:
                return(l or r)
        return(helper(root))