# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy=ListNode()
        curr=dummy
        dummy.next=head
        
        while(dummy.next and dummy.next.next):
            
            p=dummy.next
            q=dummy.next.next
        
            p.next=q.next
            q.next=p
            dummy.next=q
            
            dummy=p
            
        return curr.next