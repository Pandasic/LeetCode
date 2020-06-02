"""
132. 分割回文串 II
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
通过次数9,842提交次数23,084
在真实的面试中遇到过这道题？
"""
#沿用上一次的代码 取长度最小 #然后超时 MMP

# 动规
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dp = [len(s) for i in range(len(s) + 1)]
        
        dp[0] = -1
        for i in range(len(s)):
            for j in range(i + 1):
                if s[j:i+1] == s[j:i+1][::-1]:
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)
                    
        return dp[-1]

class Solution:
    def minCut(self, s: str):
        if s == "":
            return 0
        minLen = len(s)
        words = list(s)
        def part(words):
            minLen = min(len(words),minLen)
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
        #print(res)
        return minLen

s = Solution()
print(s.minCut("ababababababababababababcbabababababababababababa"))