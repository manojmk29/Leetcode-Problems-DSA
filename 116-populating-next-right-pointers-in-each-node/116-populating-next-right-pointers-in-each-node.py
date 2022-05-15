"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        stk=deque([])
        if(root):
            stk.append(root)
        l=0
        while(stk):
            prev=None
            n=len(stk)
            while(n):
                if(prev):
                    prev.next=stk[0]
                prev=stk.popleft()
                if(prev.left):
                    stk.append(prev.left)
                if(prev.right):
                    stk.append(prev.right)
                n-=1
        return(root)
                
        