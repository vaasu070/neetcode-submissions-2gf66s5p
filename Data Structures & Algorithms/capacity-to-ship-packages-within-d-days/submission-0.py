class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canship(cap):
            ship = 1

            curr_cap = cap

            for weight in  weights:

                if curr_cap- weight<0:
                    ship+=1
                    if ship>days:
                        return False
                    curr_cap = cap
                curr_cap-=weight
            return True
                




        l = max(weights)
        r = sum(weights)
        res  = r

        while l<=r:

            mid  = l+ (r-l)//2
            if canship(mid):
                r =  mid-1
                res = min(res ,mid)
            else:
                l = mid+1
        return res
        