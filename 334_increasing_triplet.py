class Solution:
    def increasingTriplet(self, nums):

        map = {}

        for i,v in enumerate(nums):
            if v not in map:
                map[v] =[i]
            else:
                map[v].append(i)

        sorted_map =dict(sorted(map.items()))
        
        indexes = [ i for i in sorted_map.values()]
        print(sorted_map)
        print(indexes)
        for i in range(len(indexes)):
            for j in range(len(indexes)):
                for k in range(k,len(indexes)):
                    if indexes[i]< indexes[j]<indexes[k]:
                        return True
        print(sorted_map)
        return False

nums = [5,4,3,2,1]        

# nums = [1,10,23,11,1,2,3,4,5,5,7,8]
obj = Solution()
print(obj.increasingTriplet(nums))