import heapq
 
 
class MinHeap:
 
    def __init__(self, k):
        self.pool = []
        self.k = k
 
    def add(self, n):
 
        # if the min-heap's size is less than `k`, push the current element
        # into the min-heap
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, n)
 
        # otherwise, if the current element is more than the smallest element
        # in the min-heap, remove the smallest element from the heap and
        # push the current element
        elif self.pool[0] < n:
            heapq.heappushpop(self.pool, n)
 
        # if the size of the min-heap reaches `k`, return the top element
        if len(self.pool) == self.k:
            return self.pool[0]
        else:
            return -1
 
 
# Function to find the k'th largest element in a stream
def findKthLargest(k):
 
    # create a min-heap using MinHeap class
    pq = MinHeap(k)
 
    # loop till the end-of-file (EOF) is reached
    while True:
        try:
            x = pq.add(int(input()))
            if x != -1:
                print("The k'th largest element is", x)
        except EOFError:
            break
 
 
if __name__ == '__main__':
 
    k = 3
    findKthLargest(k)
 
