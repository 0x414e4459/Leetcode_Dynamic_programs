class Solution:
    def maxProfit(self, prices) -> int:
        maxprofit=0
        stock=prices[0]
        for i in prices:
            if(i>stock):
                maxprofit=max(maxprofit,i-stock)
            stock=min(stock,i)
        return maxprofit

prices=[7,1,5,3,6,4]          
sol=Solution()
print(sol.maxProfit(prices))      
