"""
140. 单词拆分 II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
通过次数14,300提交次数37,837
在真实的面试中遇到过这道题？
"""
class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [None for i in range(len(s))]
        def wordBreakPart(begin):
            #恰好相等 正确并返回
            if begin == len(s):
                return [""]
            #超出 返回错误
            if begin > len(s):
                return None
            #缓存数组剪枝
            if dp[begin] != None:
                return dp[begin]
            res = []
            #迭代遍历
            for i in range(begin+1,len(s)+1):
                part = []
                if s[begin:i] in wordDict:
                    p = s[begin:i]
                    part = wordBreakPart(i)
                    if part != None:
                        #遍历 并添加新的词汇
                        for p in part:
                            if p == "":
                                res.append(s[begin:i])
                            else:
                                res.append(s[begin:i]+" " + p)
            dp[begin] = res
            return res
        wordBreakPart(0)
        return dp[0]


s = Solution()
print(s.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
print(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]    ))
print(s.wordBreak( "catsandog", ["cats", "dog", "sand", "and", "cat"]))