class Solution:
    def partitionLabels(self, s):
        map ={}
        output =[]
        for i,v in enumerate(s):
            if v not in map:
                map[v] = [i,i]
            else:
                map[v][1] = i
        ranges = [i for i in map.values()]
        
        start =100
        end = 100
        
        for i in ranges:
            if start == 100 and end == 100:
                start = i[0]
                end = i[1]
            elif start <i[0]< end < i[1]:
                end = i[1]
            elif start <i[0] < i[1]< end:
                pass
            elif start <= end <i[0]:
                output.append(end-start+1)
                start = i[0]
                end = i[1]
        output.append(end-start+1)        
        return output
        











# s = "ababcbacadefegdehijhklij"
s="caedbdedda"
obj = Solution()
print(obj.partitionLabels(s))