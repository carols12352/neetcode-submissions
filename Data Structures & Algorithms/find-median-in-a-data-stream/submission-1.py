class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        if len(self.left) > len(self.right) + 1:
            value = -heapq.heappop(self.left)
            heapq.heappush(self.right, value)
        elif len(self.right) > len(self.left) + 1:
            value = heapq.heappop(self.right)
            heapq.heappush(self.left, -value)        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0

        if len(self.left) > len(self.right):
            return float(-self.left[0])

        return float(self.right[0])

        
        