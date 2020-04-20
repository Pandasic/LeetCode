"""
91. 解码方法
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
通过次数39,726提交次数170,648
"""

#超时 边界处理
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1 and s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        return self.numDecodings_part(s,0,1) + self.numDecodings_part(s,0,2)

    def numDecodings_part(self,s,begin,length):
        res = 0
        if begin + length == len(s):
            w = s[begin:begin+length]
            if (0 < int(w) <=9 and length == 1) or (10<= int(w) <= 26 and length == 2):
                return 1
            else:
                return 0
        elif begin + length > len(s):
            return 0
        else:
            w = s[begin:begin+length]
            if (0 < int(w) <=9 and length == 1) or (10<= int(w) <= 26 and length == 2):
                res += self.numDecodings_part(s,begin+length,1)
                res += self.numDecodings_part(s,begin+length,2)
                return res
            else:
                return 0
s = Solution()
print(s.numDecodings("01"))