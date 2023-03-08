class Solution:
    def findRepeatedDnaSequences(self, s):
        output =set()
        counter = set()
        temp = s[:10]
        counter.add(temp)
        for i in range(10,len(s)):
            temp = temp[1:]
            temp+=s[i]
            if temp in counter: 
                output.add(temp)
            else: 
                counter.add(temp)
            
        return [i for i in output]  
        
        





s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
obj = Solution()
print(obj.findRepeatedDnaSequences(s))