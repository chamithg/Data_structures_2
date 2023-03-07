class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split(" ")
        if len(s_arr) != len(pattern):return False
        map = {}
        for i in range(len(pattern)):
            if pattern[i] in map:
                if map[pattern[i]] != s_arr[i]:
                    return False
            elif s_arr[i] in map.values():
                    for key,value in map.items():
                        if value == s_arr[i] and key != pattern[i]:
                            return False
            else:
                map[pattern[i]] = s_arr[i]
        
        return True


pattern = "abba"
s = "dog dog dog dog"
obj = Solution()
print(obj.wordPattern(pattern,s))