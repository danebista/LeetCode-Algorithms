# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root=ListNode(0, head)
        prev=root
        c=head
        while(c):
            t=c
            listindex=0
            while (c and listindex <k):
                c=c.next
                listindex+=1
                
            if listindex!=k:
                prev.next = t
            else:
                prev.next =self.reverseALinkedList(t,k)
                prev= t
        return root.next
    
    def reverseALinkedList(self, l1, k):
        p=None
        c=l1
        
        while(c and k>0):
            q=c.next
            c.next=p
            
            p=c
            c=q
            k-=1
            
        l1=p
        return l1