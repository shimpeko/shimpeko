# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0, head)
        granny = None
        mummy = None
        me = answer
        while me:
            if granny is None:
                granny = me
                me = me.next
                continue
            if mummy is None:
                mummy = me
                me = me.next
                continue
            # Swap me and mummy
            mummy.next = me.next
            me.next = mummy
            # Connect granny and me
            granny.next = me
            # Set me as mummy as me and mummy was swapped
            me = mummy
            # Forget about granny and mummy
            granny = None
            mummy = None
        return answer.next
