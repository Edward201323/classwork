# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        a_curr = headA
        while a_curr:
            s.add(a_curr)
            a_curr = a_curr.next
        
        b_curr = headB
        while b_curr:
            if b_curr in s:
                return b_curr
            b_curr = b_curr.next

        return None
