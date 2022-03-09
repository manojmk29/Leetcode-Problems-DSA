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
        pv=p.val
        qv=q.val
        while(root):
            rv=root.val
            if((pv<=rv and qv>=rv) or(pv>=rv and qv<=rv)):
                return(root)
            if(pv>rv):
                root=root.right
            else:
                root=root.left