"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def addBinary(self, a: str, b: str):
        #对齐
        maxlen = max(len(a),len(b))
        a = a.rjust(maxlen,'0')
        b = b.rjust(maxlen,'0')
        pre = 0
        res = [""]*maxlen
        for i in range(maxlen):
            r = int(a[maxlen - i - 1]) + int(b[maxlen - i - 1]) + pre
            res[maxlen - i - 1] = str(r%2)
            pre = r//2
        #最后可能进位处理
        if pre == 1:
            res = ['1'] + res
        return "".join(res)

    
s = Solution()
print(s.addBinary("11","1"))
print(s.addBinary("1010","1011"))
print(s.addBinary("1010",""))
