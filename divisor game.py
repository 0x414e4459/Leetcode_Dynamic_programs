class Solution:
    def divisorGame(self, n: int) -> bool:
      if(n%2==0): return True
      else: return False

sol=Solution()
n=int(input())
print(sol.divisorGame(n))