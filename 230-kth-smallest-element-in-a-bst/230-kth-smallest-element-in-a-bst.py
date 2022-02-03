# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        def inorder(root):
            if(root):
                inorder(root.left)
                stack.append(root.val)
                inorder(root.right)
        inorder(root)
        return(stack[k-1])