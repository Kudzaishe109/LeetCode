class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_day = 1
        max_profit = 0
        min_buying = prices[0]
        while sell_day < len(prices):
            max_profit= max(max_profit, prices[sell_day] - min_buying)
            min_buying = min(min_buying, prices[sell_day])
            sell_day += 1
        return max_profit



            
            


        