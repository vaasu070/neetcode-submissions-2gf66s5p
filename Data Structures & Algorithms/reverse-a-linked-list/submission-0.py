# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(head)
        prev = None
        curr = head


        while curr is not None:

            next_pointer = curr.next

            curr.next = prev

            # move to the next node

            prev = curr
            curr = next_pointer

        return prev
        
        