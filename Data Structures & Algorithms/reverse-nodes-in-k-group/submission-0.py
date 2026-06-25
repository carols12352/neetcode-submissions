# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy

        while True:
            kth = pre

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next

            prev = group_next
            cur = pre.next

            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            tmp = pre.next
            pre.next = kth
            pre = tmp
            
        
            
            
            
            
            
            
