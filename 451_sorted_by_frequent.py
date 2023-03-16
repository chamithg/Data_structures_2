class Solution:
    def frequencySort(self, s: str) -> str:
        map ={}
        output =""
        for i in s:
            if i not in map:
                map[i] = 1
            else:
                map[i]+=1
        sorted_map = sorted(map.items(), key=lambda x:x[1])

        for i in reversed(range(len(sorted_map))):
            output += sorted_map[i][0]*sorted_map[i][1]
        return output