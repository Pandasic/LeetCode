"""
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
通过次数95,153提交次数219,919
在真实的面试中遇到过这道题？
"""

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #去空格
        s = s.lower()
        s = "".join(re.findall("([a-z]|[0-9])",s))
        for i in range(len(s)//2):
            if s[i] != s[len(s)- i - 1]:
                return False
        else:
            return True

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(""))