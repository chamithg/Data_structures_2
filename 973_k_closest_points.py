from collections import OrderedDict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances=[]
        output =[]

        for i in points:
            total = abs(i[0])**2 +  abs(i[1])**2
            distances.append((total,i))
        distances.sort()

        for i in range(k):
            output.append(distances[i][1])

        return output