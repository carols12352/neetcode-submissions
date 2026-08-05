class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while heap and len(heap) > 1:
            large1 = -heapq.heappop(heap)
            large2 = -heapq.heappop(heap)
            res = large1 - large2
            if res:
                heapq.heappush(heap, -res)


        if heap:
            return -heapq.heappop(heap)
        else:
            return 0