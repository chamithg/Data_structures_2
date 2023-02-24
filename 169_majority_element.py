class Solution:
    def majorityElement(self, nums):
        counter ={}
        for i in nums:
            if i not in counter:
                counter[i]=1
            else:
                counter[i]+=1
        return max(counter, key=counter.get)
            
nums = [3,3,4]
obj= Solution()
print(obj.majorityElement(nums))