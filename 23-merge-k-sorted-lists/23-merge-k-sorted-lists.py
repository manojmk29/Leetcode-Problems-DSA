# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l=len(lists)
        if(l==0):
            return(None)
        def merge(s,e):
            if(e>s):
                m=(s+e)//2
                left=merge(s,m)
                right=merge(m+1,e)
                root=temp=ListNode(0)
                while(left and right):
                    if(left.val<right.val):
                        temp.next=left
                        temp=left
                        left=left.next
                        temp.next=None
                    else:
                        temp.next=right
                        temp=right
                        right=right.next
                        temp.next=None
                while(left):
                    temp.next=left
                    temp=left
                    left=left.next
                    temp.next=None
                while(right):
                    temp.next=right
                    temp=right
                    right=right.next
                    temp.next=None
                return(root.next)
            else:
                return(lists[s])
        return(merge(0,l-1))
            