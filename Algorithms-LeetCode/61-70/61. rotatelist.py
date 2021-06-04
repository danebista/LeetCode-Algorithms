# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        current = head
        count=1
        
        if not head:
            return head
        
        while (current.next):
            current=current.next
            count += 1
        current.next =head
  
        breaker = count - k % count
        current = head
        iterator=0
        
        while(iterator < breaker):
            prev=current
            current=current.next
            iterator += 1
        
        prev.next = None
        head=current
        
        return head
        