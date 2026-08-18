# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # If the linked list is empty,
        # or there is only one node,
        # or k is 0,
        # return the same linked list.
        if head == None or head.next == None or k == 0:
            return head

        # Start from the first node.
        tail = head

        # Initially, the linked list has one node.
        length = 1

        # Find the length of the linked list
        # and move tail to the last node.
        while tail.next != None:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations.
        # Example:
        # length = 5, k = 12
        # 12 % 5 = 2
        k = k % length

        # If k becomes 0,
        # no rotation is needed.
        if k == 0:
            return head

        # Start again from the head.
        curr = head

        # Find how many steps to move
        # to reach the new tail.
        #
        # Example:
        # 1 → 2 → 3 → 4 → 5
        # k = 2
        #
        # New list should be:
        # 4 → 5 → 1 → 2 → 3
        #
        # New tail is 3.
        #
        # steps = length - k - 1
        steps = length - k - 1

        # Move curr to the new tail.
        while steps > 0:
            curr = curr.next
            steps -= 1

        # The node after curr
        # becomes the new head.
        newHead = curr.next

        # Break the linked list.
        curr.next = None

        # Connect the old last node
        # to the old head.
        tail.next = head

        # Return the new head.
        return newHead