# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if not head.next.next:
            cn = head.next
            head.next.next = head
            head.next = None
            return cn
        
        
        c = head
        prev = None
        cn = c.next
        cnn = c.next.next
        
        while cnn:
            # Change direction
            c.next = prev
            cn.next = c
            
            prev = c
            c = cn

            cn = cnn
            cnn= cn.next
        cn.next = c
        return cn




        