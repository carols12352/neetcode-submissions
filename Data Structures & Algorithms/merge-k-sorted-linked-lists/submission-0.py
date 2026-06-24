# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i, node in enumerate(lists):
            heapq.heappush(h, (node.val, i , node))

        dummy = ListNode(0)
        cur = dummy

        while h:
            val, i, node = heapq.heappop(h)

            cur.next = ListNode(val)
            cur = cur.next

            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
            
        return dummy.next

        