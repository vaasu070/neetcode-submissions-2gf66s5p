class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        from heapq import heapify , heappop
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapify(minHeap)
        print(minHeap)
        res= []
        while k>0:
            print(len(minHeap), k)
            [dist, x, y]=  heappop(minHeap)
            res.append([x, y])
            k-=1
        

        return res


        