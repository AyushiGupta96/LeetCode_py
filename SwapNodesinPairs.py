#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
from typing import Optional


# Example 1:
#
# Input: head = [1,2,3,4]
#
# Output: [2,1,4,3]
#
# Explanation:
#
#
#
# Example 2:
#
# Input: head = []
#
# Output: []
#
# Example 3:
#
# Input: head = [1]
#
# Output: [1]
#
# Example 4:
#
# Input: head = [1,2,3]
#
# Output: [2,1,3]
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node