class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for day in range(len(prices)):
           min_price = min(prices[day],min_price)

           profit = prices[day] - min_price

           max_profit = max(max_profit,profit)
        
        return max_profit


        