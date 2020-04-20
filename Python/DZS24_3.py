"""
5374. 长度为 n 的开心字符串中字典序第 k 小的字符串 显示英文描述 
通过的用户数104
尝试过的用户数107
用户总通过次数104
用户总提交次数124
题目难度Medium
一个 「开心字符串」定义为：

仅包含小写字母 ['a', 'b', 'c'].
对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。
比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字符串。

给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。

请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。

 

示例 1：

输入：n = 1, k = 3
输出："c"
解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。
示例 2：

输入：n = 1, k = 4
输出：""
解释：长度为 1 的开心字符串只有 3 个。
示例 3：

输入：n = 3, k = 9
输出："cab"
解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"] 。第 9 个字符串为 "cab"
示例 4：

输入：n = 2, k = 7
输出：""
示例 5：

输入：n = 10, k = 100
输出："abacbabacb"
 

提示：

1 <= n <= 10
1 <= k <= 100
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if n == 0:
            return ""
        happyStrs = []
        def getHappyStr(s):
            if len(s) == n:
                happyStrs.append(s)
                return
            if s[-1] == "a":
                getHappyStr(s + "b")
                getHappyStr(s + "c")
            elif s[-1] == "b":
                getHappyStr(s + "a")
                getHappyStr(s + "c")
            elif s[-1] == "c":
                getHappyStr(s + "a")
                getHappyStr(s + "b")
        getHappyStr("a")
        getHappyStr("b")
        getHappyStr("c")
        if k > len(happyStrs):
            return ""
        happyStrs.sort()
        return happyStrs[k-1]

s = Solution()
print(s.getHappyString(2,7))