class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if not lists or len(lists)==0:
            return None
        while(len(lists)>1):
            newList=[]
            for i in range(0, len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                newList.append(self.mergeLists(l1,l2))
            lists=newList
        return lists[0]
    
    def mergeLists(self, l1, l2):
        dummy=ListNode()
        curr=dummy
        
        while l1 and l2:
            if l1.val>=l2.val:
                curr.next=l2
                l2=l2.next
               
            else:
                curr.next=l1
                l1=l1.next
            
            curr=curr.next
        
        if l1:
            curr.next=l1
        elif l2:
            curr.next=l2
        
        return dummy.next