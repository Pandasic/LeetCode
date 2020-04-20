"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/text-justification
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

那啥。没做出来挂个红
#先放放 刚觉没理清思路
from tools import printArray

class Solution:
    def getArrayCharsLen(self,arr):
        #获取单词数组的字符数量
        sum = 0
        for w in arr:
            sum += len(w)
        return w

    def fullJustify(self, words, maxWidth: int):
        #最终文章
        article = []
        #当前行单词的组合
        nowWords = list()
        #当前行
        nowLen = 0
        itor = 0
        while itor < len(words):
            if len(words[itor]) + nowLen <= maxWidth - len(nowWords) + 1:
                nowWords.append(words[itor])
                nowLen += len(words[itor])
                itor += 1
            else:
                if len(nowWords) == 1:
                    spaceNum  = maxWidth - nowLen
                    article.append(nowWords[0] + " " * spaceNum)
                else: 
                    #求出平均空格
                    spaceNum = (maxWidth - nowLen)//(len(nowWords) - 1)
                    extraSpace = maxWidth - nowLen - spaceNum * (len(nowWords) - 1)
                    new_line = nowWords[0]
                    for w in nowWords[1:]:
                        new_line += " "*spaceNum
                        if extraSpace > 0:
                            new_line += " "
                        new_line += w
                    article.append(new_line)
                nowLen = 0
                nowWords = []

        if nowLen > 0:
            new_line = " ".join(nowWords)
            new_line.ljust(maxWidth," ")
            article += [new_line]
        return article


def showLineWordsCount(arr):
    for line in arr:
        print(len(line))
    print()

s = Solution()
showLineWordsCount(s.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."],maxWidth = 16))
showLineWordsCount(s.fullJustify(words = ["What","must","be","acknowledgment","shall","be"],maxWidth = 16))
showLineWordsCount(s.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],maxWidth = 20))

