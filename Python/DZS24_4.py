"""
5375. 恢复数组 显示英文描述 
通过的用户数41
尝试过的用户数53
用户总通过次数41
用户总提交次数88
题目难度Hard
某个程序本来应该输出一个整数数组。但是这个程序忘记输出空格了以致输出了一个数字字符串，我们所知道的信息只有：数组中所有整数都在 [1, k] 之间，且数组中的数字都没有前导 0 。

给你字符串 s 和整数 k 。可能会有多种不同的数组恢复结果。

按照上述程序，请你返回所有可能输出字符串 s 的数组方案数。

由于数组方案数可能会很大，请你返回它对 10^9 + 7 取余 后的结果。

 

示例 1：

输入：s = "1000", k = 10000
输出：1
解释：唯一一种可能的数组方案是 [1000]
示例 2：

输入：s = "1000", k = 10
输出：0
解释：不存在任何数组方案满足所有整数都 >= 1 且 <= 10 同时输出结果为 s 。
示例 3：

输入：s = "1317", k = 2000
输出：8
解释：可行的数组方案为 [1317]，[131,7]，[13,17]，[1,317]，[13,1,7]，[1,31,7]，[1,3,17]，[1,3,1,7]
示例 4：

输入：s = "2020", k = 30
输出：1
解释：唯一可能的数组方案是 [20,20] 。 [2020] 不是可行的数组方案，原因是 2020 > 30 。 [2,020] 也不是可行的数组方案，因为 020 含有前导 0 。
示例 5：

输入：s = "1234567890", k = 90
输出：34
 

提示：

1 <= s.length <= 10^5.
s 只包含数字且不包含前导 0 。
1 <= k <= 10^9.

"""
import math
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        maxLen = int(math.log10(k)+1)
        modVal = int(10e9+7)
        dp = {"":1}
        def part(s):
            #print(s)
            res = 0
            if s in dp.keys():
                return dp[s]

            if s.startswith("0"):
                dp[s] = 0
                return 0
            for i in range(1,min(len(s),maxLen)+1):
                if int(s[:i]) <= k:
                    res += part(s[i:])
                    res = res%modVal
            dp[s] = res%modVal
            return res%modVal
        
        res = part(s)%modVal
        #print(dp)
        return res

s = Solution()
#print(s.numberOfArrays("1000",1000))
#print(s.numberOfArrays("1000",10))
#print(s.numberOfArrays("1317",2000))
#print(s.numberOfArrays("2020",30))

print(s.numberOfArrays("1234567890",90))
#print(s.numberOfArrays("263136",46))
#print(s.numberOfArrays("1111111111111",1000000000))
print(s.numberOfArrays("2553462832281151811513004352253111",456))