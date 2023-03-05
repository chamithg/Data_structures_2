class Solution:
    def increasingTriplet(self, nums):
        map = {}
        temp_min = float('inf')
        
        for i,v in enumerate(nums):
            temp_min = min(v,temp_min)
            map[i] = [temp_min,v]
        
        
        temp_max = float('-inf')
        for i in reversed(range(len(nums))):
            temp_max = max(nums[i],temp_max)
            map[i].append(temp_max)
        
        for v in map.values():
            if v[0]<v[1]<v[2]:
                return True
        
        return False
            
            
        print(map)
        


nums = [5,4,3,2,1]        

# nums = [1,10,23,11,1,2,3,4,5,5,7,8]
obj = Solution()
print(obj.increasingTriplet(nums))