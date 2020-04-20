"""
5195. 最长快乐字符串 显示英文描述 
用户通过次数0
用户尝试次数0
通过次数0
提交次数0
题目难度Medium
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。

 

示例 1：

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
示例 2：

输入：a = 2, b = 2, c = 1
输出："aabbc"
示例 3：

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。
 

提示：

0 <= a, b, c <= 100
a + b + c > 0
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        charNums = [[a,"a"],[b,"b"],[c,"c"]]
        charNums.sort(key = lambda t:t[0])
        print(charNums)
        #情况一 其他字符的总和没有第三种大

        #情况二够用
        res = ""

        charNumSum = a + b + c
        charNums.sort(key = lambda t:t[0])
        nowChar = charNums[-1][1]
        charNums.reverse()
        while charNumSum > 0:
            if (charNums[0][0] + charNums[1][0])*2 + 2 <= charNums[2][0]:
                res += (charNums[2][1]*2 + charNums[0][1])*charNums[0][0] + \
                        (charNums[2][1]*2 + charNums[1][1])*charNums[1][0] + \
                        charNums[2][1]*2
                break
            if charNums[charItor][0] >=2:
                res += charNums[charItor][1] * 2
                charNums[charItor][0] -= 2
                charNumSum -= 2
            elif charNums[charItor][0] == 1 :
                res += charNums[charItor][1]
                charNums[charItor][0] -= 1
                charNumSum -= 1
            else:
                pass
        return res

s =Solution()
print(s.longestDiverseString(2,4,1))