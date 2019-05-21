"""
5065. 最长字符串链  
给出一个单词列表，其中每个单词都由小写英文字母组成。
如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。
词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。
从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。

示例：

输入：["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 "a","ba","bda","bdca"。
 

提示：

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] 仅由小写英文字母组成。
 
"""

"""
动态规划的题目
"""
class Solution:
    def __init__(self):
        self.max_len = 0
        self.dp = {}
    def longestStrChain(self, words = []) -> int:
        len_dict = [[] for i in range(20)]#单词最长为16
        for i in range(len(words)):
            len_dict[len(words[i])].append(words[i])
        for i in range(len(len_dict)-1,-1,-1):
            for w in len_dict[i]:
                self.find_longestStrChain(w,len_dict)
        print(self.dp)
        for v in self.dp.values():
            self.max_len = max(self.max_len,v)
        return self.max_len

    def find_longestStrChain(self, word,len_dict):
        max_v = 1
        for w in len_dict[len(word) + 1]:
            if self.isNext(word,w):
                if w in self.dp.keys():
                    max_v = max(max_v,self.dp[w]+1)
        self.dp[word] = max_v
        return max_v

    #检测是否符合磁链的需求  
    def isNext(self,f,b):
        offset = 0
        i = 0
        while (i<len(f)):
            if f[i] == b[i + offset]:
                i += 1
            else:
                offset += 1
                if (offset >1):
                    return False
        return True

s = Solution()
print(s.longestStrChain(
    ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
    ))

