# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        
        # curr = head
        # count = 0
        # match_node=None
        # while True:

        #     if match_node == curr.next:
        #         return True

        #     if count==index:
        #         match_node = curr

        #     curr = head.next

        #     count+=1


        # apporach 1
    
        # hash = set()

        # curr= head

        # while curr:
        #     if curr in hash:
        #         return True
        #     hash.add(curr)
        #     curr = curr.next

        # return False
            

        # approach 2:

        slow=  head
        fast = head


        while fast and fast.next:

            
            slow= slow.next
            fast = fast.next.next

            if slow==fast:
                return True
        return False






        