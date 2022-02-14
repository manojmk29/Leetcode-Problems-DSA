class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret=[]
        def helper(root):
            if (root):
                ret.append(str(root.val))
                left=helper(root.left)
                right=helper(root.right)
            else:
                ret.append("N")
        helper(root)
        return ' '.join(ret)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            v=next(arr)
            if(v=="N"):
                return(None)
            node=TreeNode(int(v))
            node.left=helper()
            node.right=helper()
            return(node)
        arr=iter(data.split())
        return(helper())
        