# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root=head=ListNode()
        carry=0
        while(l1 or l2):
            fir=0
            sec=0
            if(l1):
                fir=l1.val
                l1=l1.next
            if(l2):
                sec=l2.val
                l2=l2.next
            tot=fir+sec+carry
            v=tot%10
            root.next=ListNode()
            root=root.next
            root.val=v
            carry=tot//10
        if(carry):
            root.next=ListNode(carry)
        return(head.next)
        # while(root):
        #     temp=root.next
        #     root.next=prev
        #     prev=root
        #     root=temp
        # return(prev)
        