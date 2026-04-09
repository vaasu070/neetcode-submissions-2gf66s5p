class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        # res = {}
        # for x in piles:
        #     k = x

        #     hour=0

            

        #     for pile in piles:
        #         print(k, math.ceil(pile/k) )
        #         hour= hour +  math.ceil(pile/k) 

        #     res[k]=hour

        # print(res)
        
        # final_output= 1000000
        # for k, item in res.items():
        #     if item<=h:
        #         final_output = min(final_output,k)
        # return final_output


        l = 1
        r = max(piles)

        res= r

        while l<=r:
            k = l+ (r-l)//2
            time = 0

            for pile in piles:
                time = time + math.ceil(pile/k)
            
            if time<=h:
                res =k
                r =k-1
            else:
                l = k+1
        return res


                

        


