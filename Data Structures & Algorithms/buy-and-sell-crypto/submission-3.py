class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l , r = 0,1

        profit = 0

        while r<=len(prices)-1:
            diff = prices[r] - prices[l]
            
            profit = max(diff , profit)
            if diff== 0:
             
                r+=1


            elif diff>0:
                r+=1
            else:
                l=r
                r+=1

        return profit
        