from collections import deque
class Solution:
    def connect(self, root):
        def helper(node):
            if(node):
                if(node.left):
                    node.left.next=node.right
                    if(node.next):
                        node.right.next=node.next.left
                helper(node.left)
                helper(node.right)
            return(node)
        return(helper(root))