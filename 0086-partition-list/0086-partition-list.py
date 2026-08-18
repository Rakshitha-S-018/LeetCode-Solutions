# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Dummy node for the list containing
        # values smaller than x.
        smallDummy = ListNode(0)

        # Dummy node for the list containing
        # values greater than or equal to x.
        largeDummy = ListNode(0)

        # These pointers help us build the two lists.
        small = smallDummy
        large = largeDummy

        
        curr = head

        #imp
        while curr != None:

           
            if curr.val < x:
                small.next = curr
                small = small.next

           
            else:
                large.next = curr
                large = large.next

            # Move to the next node.
            curr = curr.next

       #connecting large.next to none to avoid repetitions
        large.next = None


        
        
        # small.next = largeDummy.next
        # Suppose the large list is:
        # largeDummy → 4 → 3 → 5
        
        # largeDummy → 4 → 3 → 5
        #                         ↑
        #                       large
        #
        
        # Therefore:
        small.next = largeDummy.next
        return smallDummy.next