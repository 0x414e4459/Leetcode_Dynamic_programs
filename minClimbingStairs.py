class Solution:
    def minCostClimbingStairs(self, cost) -> int:       #bottom-up approach
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
    
    def minCostClimbingStairs2(self, cost) -> int:   #top-booto appraoch
        def totalCost(n):
            if(n<2):
                return cost[n]
            else:
                return cost[n]+min(totalCost(n-1),totalCost(n-2))
        return min(totalCost(len(cost)-1),totalCost(len(cost)-2))

sol=Solution()
cost=[10,15,20]
print(sol.minCostClimbingStairs2(cost))