class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = right - left
        left = 0
        right = 1
        
        max_profit = 0
        while right< len(prices):
            profit = prices[right] - prices[left]

            if prices[right] > prices[left]:
                print(left,right)
                max_profit = max(profit, max_profit)
            else:
                left = right
            
            right += 1


        return max_profit