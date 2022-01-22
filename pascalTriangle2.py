class Solution:
    def getRow(self, rowIndex: int):
        arr=[]
        for i in range(rowIndex+1):
            temp=[0]*(i+1)
            for j in range(i+1):
                if(j==0 or j==i):
                    temp[j]=1
                else:
                    temp[j]=arr[i-1][j-1]+arr[i-1][j]
            arr.append(temp)
        return arr[-1]

sol=Solution()
n=int(input())
print(sol.getRow(n))
