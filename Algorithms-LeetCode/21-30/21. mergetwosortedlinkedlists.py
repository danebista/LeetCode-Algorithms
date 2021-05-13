class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if (l1.val>l2.val):
            head=l2
            l2=l2.next
        else:
            head=l1
            l1=l1.next
        
        current=head
        
        while(l1 and l2):
            if l1.val>=l2.val:
                current.next=l2
                current=current.next
                l2=l2.next
            else:
                current.next=l1
                current=current.next
                l1=l1.next
        
        if 11:
            current.next=l1
        if l2:
            current.next=l2
            
        return head
        