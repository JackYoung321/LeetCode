# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Understanding of theory
#print(list1) :
#ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
#print(list1.next) :
#ListNode{val: 2, next: ListNode{val: 4, next: None}}}


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy #Make tail a list node, leaving dummy as the first value

        while list1 and list2: #While both lists are not empty
            
            if list1.val < list2.val: #If the head value in list 1 is smaller than the head val in list 2
                tail.next = list1 #Set the 'next' portion of tail to list1, effectively adding the head of list1

                list1 = list1.next#Move along to the next value in line in list1 
                
            else: # The above but if the head value in list 2 is smaller than the one in list 1
                tail.next = list2 
                list2 = list2.next
            print(tail)
            tail = tail.next #Update the "pointer" to the next box along, setting the current val to the just added
                            
          
        if list1: # If either list was longer than the other, add the remaining leftover (already sorted) values to the                     end
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next #Use dummy.next to return the head of the newly sorted list (initialising dummy first
                          #defines the first node at the beginning of the list)
        
