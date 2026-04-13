from heapq import heapify, heappush , heappop 

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.min_heap  = nums
        heapify(self.min_heap)
        self.size = k

        while len(self.min_heap)>self.size:
            heappop(self.min_heap)
            
        

    def add(self, val: int) -> int:
        heappush(self.min_heap  , val)
        
        if len(self.min_heap)>self.size:
            heappop(self.min_heap)
        return self.min_heap[0]
            



        
