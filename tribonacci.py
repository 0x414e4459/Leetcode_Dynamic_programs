
class Solution:
    memo={}
    def tribonacci(self, n: int) -> int:
        if(n==0):
            return 0
        elif(n<=2):
            return 1
        else:
            if n not in self.memo:
                val=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
                self.memo[n]=val
                return val
            else:
                return self.memo[n]

sol=Solution()
print('enter the value of n: ',end='')
n=int(input())
print('tribonacci of '+str(n)+' is: '+str(sol.tribonacci(n)))
# print(sol.memo)