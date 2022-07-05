# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head #Initialise slow and fast at the start position as a list head
        
        while fast and fast.next: #While fast and the node following exists, this is to ensure there are enough
                                #Nodes to iterate through, if there isn't then there is no cycle as the list stops 
                                #(due to further nodes not existing)
            slow = slow.next # Iterate 1 forwarsd
            fast = fast.next.next # Iterate 2 forwards
            if slow == fast: #Due to a 'phase difference' between fast and slow, if there is a cycle there will be
                            #a point where fast and slow reach the same point, therefore return True
                return True
        return False # False will be returned by default as if we can't continue iterating through (using fast as fast
                    #iterates through twice as fast as slow, therefore would reach the end of the list first)

#Solved with O(n) (linear) time complexity as dependant on the amount of n elements in the list
#Solved using O(1) space complexity (Constant memory) as the method used for checking the values does not result in an increase of space use with more elements in the list.
