# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        list1 = prev
        list2 = head
        while list1:
            temp1 = list2.next
            temp2 = list1.next

            list2.next = list1
            list1.next = temp1

            list2 = temp1
            list1 = temp2
        
        
