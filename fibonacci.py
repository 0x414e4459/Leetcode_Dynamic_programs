class Solution:
    def fib1(self, n: int) -> int:     #tabulation(bottom-up approach)
        fib=[0,1]
        for i in range(2,n+1):
            val=fib[i-1]+fib[i-2]
            fib.append(val)    
        return fib[n]
    
    def fib2(self,n:int)->int:     #memoization(top-bottom approach)
        if(n==0):
             return 0
        elif(n<=2):
            return 1
        if n in memo:
            return memo[n]
        else:
            val= self.fib2(n-1)+self.fib2(n-2)
            memo[n]=val
            return val

a=Solution()
memo={}
print('enter the value of n:',end=' ')
n=int(input())
print(a.fib2(n))
print(a.fib1(n))
