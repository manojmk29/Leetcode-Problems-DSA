class Solution(object):
    def deleteDuplicates(self, head):
        if(not head or not head.next):
            return(head)
        ret=temp=ListNode(0)
        val=head.val
        count=1
        head=head.next
        while(head):
            if(head.val==val):
                count+=1
            else:
                if(count<2):
                    temp.next=ListNode(val)
                    temp=temp.next
                val=head.val
                count=1
            head=head.next
        if(temp.val!=val and count<2):
                temp.next=ListNode(val)
        return(ret.next)