# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        templist=head
        l=self.findLengthOfLinkedList(templist)
        m=l-n-1
        
        iteratorlist=head
        if m<=0 and l==n:
            head=head.next
            return head
        
        for i in range(m):
            iteratorlist=iteratorlist.next
        
        iteratorlist.next = iteratorlist.next.next
        
        return head
            
    def findLengthOfLinkedList(self, lists:ListNode)->int:
        c=0
        while (lists):
            c=c+1
            lists=lists.next
            
        return c
        