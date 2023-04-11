# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr= answer = ListNode(0, head)
        batch_head = curr
        loop_count = 0
        while curr.next:
            loop_count = loop_count + 1
            if loop_count != 0 and loop_count % k == 0:
                batch_curr = batch_head.next
                for i in range(k-1):
                    tmp = batch_curr.next.next
                    batch_curr.next.next = batch_head.next
                    batch_head.next = batch_curr.next
                    batch_curr.next = tmp
                curr = batch_head = batch_curr
            else:
                curr = curr.next
        return answer.next