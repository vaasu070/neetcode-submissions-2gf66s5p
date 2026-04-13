class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        from heapq import heapify , heappush , heappop

        stones = [-s for s in stones]
        heapify(stones)

        while len(stones)>1:

            x = heappop(stones)
            y = heappop(stones)
            if y>x:
                diff= x -y
                heappush(stones , diff)
        
        stones.append(0)
        return abs(stones[0])
        





        