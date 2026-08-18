# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head

        dummy=ListNode(0)
        prev=dummy
        dummy.next=head

        if head==None:
            return None

        while curr is not None and curr.next is not None:
            if curr.val==curr.next.val:
                while curr and curr.next and curr.val==curr.next.val:
                    curr=curr.next
                curr=curr.next #for edge cases
                prev.next=curr #rerouting next pointer
            else:
                prev=curr
                curr=curr.next
                
        return dummy.next        