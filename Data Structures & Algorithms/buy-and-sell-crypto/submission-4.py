class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        profit = 0
        while l<r and r<len(prices):
            profit_total = prices[r] - prices[l]
            print(profit_total, l , r)

            if profit_total<0:
                l = r
                r+=1
            elif profit_total>=0:
                r+=1
            
            profit = max(profit, profit_total)
        return profit

        