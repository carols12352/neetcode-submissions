# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cnt = head
        while cnt:
            length += 1
            cnt = cnt.next
        dummy = ListNode(0)

        dummy.next = head

        cur = head
        prev = dummy
        cnt2 = 0
        while cur:
            if cnt2 == length - n:
                prev.next = cur.next
            prev = cur
            cur = cur.next
            cnt2 += 1
        return dummy.next

                

        