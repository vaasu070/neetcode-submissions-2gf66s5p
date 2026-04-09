# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1=[]
        curr = l1
        while curr:
            n1.append(str(curr.val))
            curr = curr.next
        n2=[]
        curr = l2
        while curr:
            n2.append(str(curr.val))
            curr = curr.next
        
        n1  = ''.join(n1[::-1])
        n2  = ''.join(n2[::-1])

        res = int(n1) + int(n2)
        print(res)

        node = ListNode()
        head = node
        for i , val in enumerate(str(res)[::-1]):
            node.val = int(val)
            if i < len(str(res))-1:   
                node.next = ListNode()
                node = node.next
        
    
        
        return head



