class Solution:
    def increasingTriplet(self, nums):

        map = {}

        for i,v in enumerate(nums):
            if v not in map:
                map[v] =[i]
            else:
                map[v].append(i)

        sorted_map =dict(sorted(map.items()))
        print(sorted_map)



nums = [1,10,23,11,1,2,3,4,5,5,7,8]
obj = Solution()
print(obj.increasingTriplet(nums))