class Solution:
    #两数相乘，最大位数不会超过他两之和，并且若两数都不为0，结果那么最多只会前面多一个0；
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = 0
        for k1,v1 in enumerate(num1):
            for k2,v2 in enumerate(num2):
                res += 10**(len(num1)-k1+len(num2)-k2-2)*int(v1)*int(v2)
        return str(res)

s = Solution()
print(s.multiply("123","321"))