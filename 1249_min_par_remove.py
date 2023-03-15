class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack =[]
        s_arr = [i for i in s]
        print(s_arr)
        for i in range(len(s_arr)):
            if s_arr[i]== "(":
                stack.append(i)
            elif s_arr[i] ==")":
                if stack:
                    stack.pop()
                else:
                    s_arr[i]=""
        for j in stack:
            s_arr[j] = ""
                    
        return "".join(s_arr)
            
        


s = "lee(t(c)o)de)"

obj = Solution()
print(obj.minRemoveToMakeValid(s))