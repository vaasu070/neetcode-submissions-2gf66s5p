class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        def get_rate(piles,k):
            res =0

            for pile in piles:
                res+=math.ceil(float(pile)/k)
            return res

       
        print(piles)
        
        l =1
        r  = max(piles)
        res = r
        while l<=r:

            k = (l + r) // 2

            total_hrs = 0
            for p in piles:
                total_hrs += math.ceil(float(p) / k)
           

            if total_hrs<=h:
                res = k
                r = k-1
               
            elif total_hrs>h:
                l = k+1
           
        return res
               
            

