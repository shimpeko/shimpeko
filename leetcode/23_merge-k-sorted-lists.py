# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numbers = []
        for l in lists:
            while l:
                numbers.append(l.val)
                l = l.next
        numbers.sort()
        answer = current_node = ListNode()
        for n in numbers:
            current_node.next = ListNode(n)
            current_node = current_node.next
        return answer.next
                    