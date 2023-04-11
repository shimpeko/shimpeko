# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_to_remove = None
        node_to_update = None
        current_node = head
        current_node_idx = 1
        # loop while current not is not None
        while current_node:
            # When idx = n then remove "head"
            # For example [1,2,3] and n = 3
            # When current node = 3 remove 1
            # No "node_to_update" in this case
            if current_node_idx == n:
                node_to_remove = head
            # When idx > n
            # For example [1,2,3] and n = 2
            # When current_node = 3 set node_to_update as 1
            # and node_to_remove as 2
            if current_node_idx > n:
                node_to_update = node_to_remove
                node_to_remove = node_to_remove.next
            current_node = current_node.next
            current_node_idx = current_node_idx + 1
        # Special case when length of list = 1 and n = 1
        if current_node_idx == 1:
            return
        # When length of list = n and n = n
        if node_to_update is None:
            return node_to_remove.next
        node_to_update.next = node_to_remove.next
        return head
