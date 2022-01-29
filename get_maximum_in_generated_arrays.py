class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums=[0,1]
        max=0
        if(n<=1):
            return n
        for i in range(2,n+1):
            if(i%2==0):
                val=nums[i//2]
            else:
                val=nums[i//2]+nums[(i//2)+1]
            if(val>max):
                max=val
            nums.append(val)
        return max

n=int(input())
sol=Solution()
print(sol.getMaximumGenerated(n))