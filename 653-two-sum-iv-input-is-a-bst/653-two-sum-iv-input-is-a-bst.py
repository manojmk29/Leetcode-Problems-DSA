# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        hset=set()
        def inorder(root):
            if root:
                if k-root.val in hset:
                    return(True)
                hset.add(root.val)
                return(inorder(root.left) or inorder(root.right))
            else:
                return False
        return(inorder(root))