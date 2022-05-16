from collections import deque
class Solution:
    def connect(self, root):
        head=root
        while(root):
            cur,root=root,root.left
            while(cur):
                if(cur.left):
                    cur.left.next=cur.right
                    if(cur.next):
                        cur.right.next=cur.next.left
                else:
                    break
                cur=cur.next
        return(head)
        