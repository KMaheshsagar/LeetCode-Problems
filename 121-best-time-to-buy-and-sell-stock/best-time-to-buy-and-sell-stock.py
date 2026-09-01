class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            profit=prices[i]-buy
            if profit>maxprofit:
                maxprofit=profit
        return maxprofit 
        