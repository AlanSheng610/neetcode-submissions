class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        largest = -heapq.heappop(self.small)

        heapq.heappush(self.large, largest)

        if len(self.large) > len(self.small):
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)


        
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large) + 1:
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/ 2.0

        