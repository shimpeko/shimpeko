# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        move_up = 0
        n = l1.val + l2.val
        if n >= 10:
            move_up = 1
            n = n - 10
        head = ListNode(n, None)
        curr = head
        while l1.next or l2.next:
            n = 0
            if l1.next:
                l1 = l1.next
                n = n + l1.val 
            if l2.next:
                l2 = l2.next
                n = n + l2.val
            n = n + move_up
            if n >= 10:
                move_up = 1
                n = n - 10
            else:
                move_up = 0
            curr.next = ListNode(n, None)
            curr = curr.next
        if move_up:
            curr.next = ListNode(move_up, None)
        return head
