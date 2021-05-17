from heapq import heapify, heappush, heappop, heappushpop

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.k_heap = nums
        heapify(self.k_heap)
        while len(self.k_heap) > k:
            heappop(self.k_heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.k_heap) < self.k:
            heappush(self.k_heap, val)
        else:
            heappushpop(self.k_heap, val)
        return self.k_heap[0]
