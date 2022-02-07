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
        self.cnt=0
        def inorder(root):
            if(root):
                left=inorder(root.left)
                if(left!=None):
                    return(left)
                self.cnt+=1
                if(self.cnt==k):
                    return(root.val)
                right=inorder(root.right)
                if(right!=None):
                    return(right)
                else:
                    return(None)
            else:
                return(None)
        return(inorder(root))
            
            
            
#         self.ctr=0
#         def inorder(root):
#             if(root):
#                 a=inorder(root.left)
#                 if(a!=None):
#                     return(a)
#                 self.ctr+=1
#                 if(self.ctr==k):
#                     return(root.val)
#                 b=inorder(root.right)
#                 if(b!=None):
#                     return(b)
#             else:
#                 return(None)
#         return(inorder(root))        
                
                
                
        # method 1
        
        # stack=[]
        # def inorder(root):
        #     if(root):
        #         inorder(root.left)
        #         stack.append(root.val)
        #         inorder(root.right)
        # inorder(root)
        # return(stack[k-1])