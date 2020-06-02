"""
5386. 检查一个字符串是否可以打破另一个字符串 显示英文描述 
通过的用户数469
尝试过的用户数568
用户总通过次数511
用户总提交次数809
题目难度Medium
给你两个字符串 s1 和 s2 ，它们长度相等，请你检查是否存在一个 s1  的排列可以打破 s2 的一个排列，或者是否存在一个 s2 的排列可以打破 s1 的一个排列。

字符串 x 可以打破字符串 y （两者长度都为 n ）需满足对于所有 i（在 0 到 n - 1 之间）都有 x[i] >= y[i]（字典序意义下的顺序）。

 

示例 1：

输入：s1 = "abc", s2 = "xya"
输出：true
解释："ayx" 是 s2="xya" 的一个排列，"abc" 是字符串 s1="abc" 的一个排列，且 "ayx" 可以打破 "abc" 。
示例 2：

输入：s1 = "abe", s2 = "acd"
输出：false 
解释：s1="abe" 的所有排列包括："abe"，"aeb"，"bae"，"bea"，"eab" 和 "eba" ，s2="acd" 的所有排列包括："acd"，"adc"，"cad"，"cda"，"dac" 和 "dca"。然而没有任何 s1 的排列可以打破 s2 的排列。也没有 s2 的排列能打破 s1 的排列。
示例 3：

输入：s1 = "leetcodee", s2 = "interview"
输出：true
 

提示：

s1.length == n
s2.length == n
1 <= n <= 10^5
所有字符串都只包含小写英文字母。

"""
#喜提超时
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def strSort(s,isReverse = False):
            s = list(s)
            s.sort(reverse = isReverse)
            return "".join(s)

        def canBreak(s1,s2):
            #s1 作为进攻 S2 防守
            s1 = strSort(s1)
            s2 = strSort(s2)
            ls1 = list(s1)
            ls2 = list(s2)
            #寻找刚好超过他的
            for i in range(len(ls1)):
                breakIndex = 0
                for j in range(breakIndex,len(ls2)):
                    if ls2[j] <= ls1[i]:
                        pass
                    else:
                        breakIndex = j
                        #此处不能打破
                        if j <= i:
                            return False
            return True

        return canBreak(s1,s2) or canBreak(s2,s1)


s = Solution()
print(s.checkIfCanBreak("abc","xya"))
print(s.checkIfCanBreak("abe","acd"))
print(s.checkIfCanBreak("leetcodee","interview"))