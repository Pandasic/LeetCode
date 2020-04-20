"""
115. 不同的子序列
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2:

输入: S = "babgbag", T = "bag"
输出: 5
解释:

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
通过次数11,454提交次数24,134
在真实的面试中遇到过这道题？
"""

#回溯
class Solution:
    def __init__(self):
        self.res = 0
    def numDistinct(self, s: str, t: str) -> int:

        def numDistinct_part(s,s_begin,t,t_itor):
            if t_itor == len(t):
                self.res += 1
                return True
            elif s_begin >= len(s) or t_itor > len(t):
                return False
            for i in range(s_begin,len(s)):
                if s[i] == t[t_itor]:
                    numDistinct_part(s,i+1,t,t_itor +1)
        
        numDistinct_part(s,0,t,0)
        return self.res

s = Solution()
print(s.numDistinct("babgbag","bag"))