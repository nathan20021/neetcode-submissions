# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        if not p1 and not p2:
            return p1
        c = ListNode()
        res = c
        while p1 or p2:
            p1_val = float("Inf") if not p1 else p1.val
            p2_val = float("Inf") if not p2 else p2.val

            if p1_val < p2_val:
                c.val = p1_val
                p1 = p1.next if p1 else None
            else:
                c.val = p2_val
                p2 = p2.next if p2 else None
            if not p1 and not p2:
                break
            c.next = ListNode()
            c = c.next


        return res