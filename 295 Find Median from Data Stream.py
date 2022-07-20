# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.minHeap) == 0 or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            temp = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, temp)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -temp)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return float(-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return -self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()