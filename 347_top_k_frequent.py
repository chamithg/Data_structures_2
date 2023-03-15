class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        output = []
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i]+=1
        
        sorted_map = sorted(map.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            output.append(sorted_map[i][0])
        
        return output

