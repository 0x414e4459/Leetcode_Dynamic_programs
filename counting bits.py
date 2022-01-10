# Given an integer n, return an array ans of length n + 1 such that for each 
# i (0 <= i <= n),  ans[i] is the number of 1's in the binary representation of i.


class Solution:
    def countBits(self, n: int):      # no dynamic programming
       ans=[]
       for i in range(0,n+1):
           a=bin(i)
           a=a[2:].count('1')
           ans.append(a)
       return ans

    def countBits2(self,n:int):    #dynamic progrgmming
        ans=[0]
        for i in range(1,n+1):
            val=ans[i//2]+(i%2)
            ans.append(val)
        return ans

a=Solution()
print('enter the value of n:',end=' ')
n=int(input())
li=a.countBits2(n)
print(li)