# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        hmap=defaultdict(int)
        def inorder(root,maxt):
            if root:
                left=inorder(root.left,maxt)
                hmap[root.val]+=1
                maxt=max(maxt,hmap[root.val])
                maxt=max(maxt,left)
                right=inorder(root.right,maxt)
                maxt=max(left,right)
                return(maxt)
            else:
                return(maxt)
        maxt=inorder(root,1)
        ret=[]
        for i in hmap:
            if hmap[i]==maxt:
                ret.append(i)
        return(ret)
                
    
        
    
#         arr=[]
#         hmap={}
#         def helper(root,count=0):
#             if(not root):
#                 return(None)
#             if(root.left and root.left.val==root.val):
#                 return(root.val)
#             if(root.right and root.right.val==root.val):
#                 return(root.val)
#             return(helper(root.left) or helper(root.right))
#         val=helper(root)
#         if(val):
#             return(val)
#         else:
#             return(ret)
            