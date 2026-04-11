# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
from typing import List

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode(0,head)
        #predecessor = last node
        #before the sublist of duplicates
        pred = sentinel
        while head:
            #if its the beginning of duplicates sublist
            #skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                #skip all duplicates
                pred.next = head.next
            #otherwise, move predecessor
            else:
                pred = pred.next
            # move forward
            head = head.next
        return sentinel.next