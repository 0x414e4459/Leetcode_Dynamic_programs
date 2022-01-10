class Solution:
    def generate(self, numRows: int) :
        res=[]
        rowSize=1
        for i in range(numRows):
            temp=[]
            for j in range(rowSize):
                if(j==0 or j==rowSize-1):
                    temp.append(1)
                else:
                    val=res[i-1][j-1]+res[i-1][j]
                    temp.append(val)
            rowSize+=1
            res.append(temp)
        return res

sol=Solution()
n=int(input())
res=sol.generate(n)
for i in res:
    for j in i:
        print(j,end=' ')
    print("")