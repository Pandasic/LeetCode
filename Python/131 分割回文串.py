"""
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
通过次数28,705提交次数42,949
"""
class Solution:
    def partition(self, s: str):
        if s == "":
            return []
        res = []
        words = list(s)
        def part(words):
            if words not in res:
                res.append(words)
            else:
                return
            if len(words)>=2 and words[0] == words[1]:
                newwords = [words[0]+words[1]] + words[2:]
                part(newwords)
            for i in range(1,len(words)-1):
                #左右两边相等
                if words[i-1] == words[i+1]:
                    newwords = words[:]
                    newwords = words[:i-1] + [words[i-1]+words[i]+words[i+1]] + words[i+2:]
                    part(newwords)
                if words[i+1] == words[i]:
                    newwords = words[:]
                    newwords = words[:i] + [words[i]+words[i+1]] + words[i+2:]
                    part(newwords)
        part(words)
        return res

s =Solution()
print(s.partition(""))