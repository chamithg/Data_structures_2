class Solution:
    def productExceptSelf(self, nums):
        prefix =1
        postfix = 1
        out = [1]*len(nums)
        pre_arr = [1]*len(nums)
        post_arr = [1]*len(nums)
        for i in range(len(nums)):
            prefix = prefix * nums[i]
            pre_arr[i] = prefix
            postfix = postfix * nums[len(nums)-1-i]
            post_arr[len(nums)-1-i] = postfix
            
            if i ==0 or i == len(nums)-1:
                pass
            else:
                out[i] = pre_arr[i-1] * post_arr[i+1]
                out[len(nums)-1-i] = pre_arr[len(nums)-2-i] * post_arr[len(nums)-i]
            
        out[0] = post_arr[1]
        out[-1] = pre_arr[-2]
        print(pre_arr,post_arr,out)
    
    
nums = [1,2,3,4]
# nums = [1,2,6,24]
# nums = [24,24,12,4]
# nums = [24,12,8,6]
obj = Solution()    
print(obj.productExceptSelf(nums))    