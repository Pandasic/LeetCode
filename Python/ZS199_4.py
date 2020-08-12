"""
5462. 压缩字符串 II 显示英文描述 
通过的用户数24
尝试过的用户数150
用户总通过次数24
用户总提交次数334
题目难度Hard
行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。

注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。

给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。

请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。

 

示例 1：

输入：s = "aaabcccd", k = 2
输出：4
解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。
示例 2：

输入：s = "aabbaa", k = 2
输出：2
解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。
示例 3：

输入：s = "aaaaaaaaaaa", k = 0
输出：3
解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。
 

提示：

1 <= s.length <= 100
0 <= k <= s.length
s 仅包含小写英文字母
"""

# 背包问题
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def getVal(count):
            if count == 1:
                return 1

            res = 1
            while count >= 1:
                res += 1
                count = count/10
            return res
            
        parts = []
        nowChar = ''
        nowCount = 0
        resLen = 0
        for i in range(len(s)):
            c = s[i]
            if nowChar == c:
                nowCount += 1
            else:
                parts.append((nowChar,nowCount,getVal(nowCount),i - nowCount))
                resLen += getVal(nowCount)
                nowChar = c
                nowCount = 1
        parts.append((nowChar,nowCount,getVal(nowCount),i - nowCount))
        resLen += getVal(nowCount)
        parts = parts[1:]
        
        
        weight=[p[1] for p in parts]
        value=[p[2] for p in parts]
        weight_most=k
        def bag_0_1(weight,value,weight_most):
            num = len(weight)
            weight.insert(0,0)
            value.insert(0,0)
            bag=np.zeros((num+1,weight_most+1),dtype=np.int32)
            for i in range(1,num+1):
                for j in range(1,weight_most+1):
                    if weight[i]<=j:
                        bag[i][j]=max(bag[i-1][j-weight[i]]+value[i],bag[i-1][j])
                    else:
                        bag[i][j]=bag[i-1][j]
            return bag[-1,-1]
        
        resLen -=bag_0_1(weight,value,weight_most)

        return resLen
s = Solution()
print(s.getLengthOfOptimalCompression("aaabcccd",2))