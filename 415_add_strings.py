class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length = max(len(num1), len(num2))

        outStr = ""

        carry_over = 0
        for i in range(length):
            n1 = 0
            n2 = 0
            if i< len(num1): n1 = int(num1[::-1][i])
            if i< len(num2): n2 = int(num2[::-1][i])

            pos_sum = n1+n2+carry_over
            if pos_sum> 9:
                carry_over = pos_sum // 10
                pos_sum = pos_sum % 10
            else:
                carry_over = 0

            outStr = str(pos_sum) + outStr
        
        if carry_over: outStr = str(carry_over) + outStr

        return outStr