class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0 
        sell_day =  1
        max_profit = 0
        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                profit = -prices[buy_day] +  prices[sell_day]
                max_profit = max(max_profit, profit)
            else:
                buy_day = sell_day
            sell_day += 1
        return max_profit


            
            


        
        