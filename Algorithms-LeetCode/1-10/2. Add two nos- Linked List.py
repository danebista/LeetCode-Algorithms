"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumofNos=int(self.numberReverser(l1)) +int(self.numberReverser(l2))
        print(sumofNos)
      
        l3=newList=ListNode(0)
        if sumofNos==0: return newList
        while (sumofNos):
    
            newList.next=ListNode(sumofNos % 10)
            newList=newList.next
            sumofNos=sumofNos // 10
       
        return l3.next
            
    def numberReverser(self,list1:ListNode)-> str:
        s1=''
   
        while(list1):
            
            s1=str(list1.val) + s1
            
            list1=list1.next
        
        return s1
        