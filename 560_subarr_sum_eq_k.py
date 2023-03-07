class Solution:
    def subarraySum(self, nums,k):
        
        
        #  this is a solid working solution but still slove for leetcode standards.
        arr_count = 0
        sum = 0
        map ={}
        for i in range(len(nums)):
            sum += nums[i]
            map[i] = sum
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i == 0: 
                    if map[j] == k: arr_count+=1
                else: 
                    if map[j]- map[i-1] == k: arr_count+=1
        
                    
        print(map)
        return arr_count




nums = [1,2,3]
k=3
obj  = Solution()
print(obj.subarraySum(nums,k))