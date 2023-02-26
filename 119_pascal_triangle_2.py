class Solution:
    def getRow(self, rowIndex):
        output = []
        for i in range(rowIndex+1):
            if i ==0 : output.append([1])
            elif i ==1 : output.append([1,1])
            else:
                temp = []
                temp.append(1)
                for j in range(len(output[i-1])-1):
                    temp.append(output[i-1][j] +output[i-1][j+1] )
                temp.append(1)
                output.append(temp)    
        return output[rowIndex]
        
        
        

rowIndex = 3
obj = Solution()
print(obj.getRow(rowIndex))
