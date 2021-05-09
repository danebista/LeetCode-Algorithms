# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l3=head  
        l=self.findLengthOfLinkedList(l3)
        if l==1 and n==1:
            head.next= None
            head.val= ''
            return head
        
        m=l-n-1
      
        if m<=0 and l==n:
            head=head.next
            return head
        elif m<=0 and l!=n:
            head.next=head.next.next
            return head
        
        l4=head
        for i in range(m):
            l4=l4.next
        
        l4.next=l4.next.next
        
        return head
    
    
    
    
    
    
    def findLengthOfLinkedList(self, lists:ListNode)->int:
        c=0
        while (lists):
            c=c+1
            lists=lists.next
            
        return c