"""
5409. 检查一个字符串是否包含所有长度为 K 的二进制子串 显示英文描述 
通过的用户数329
尝试过的用户数439
用户总通过次数329
用户总提交次数565
题目难度Medium
给你一个二进制字符串 s 和一个整数 k 。

如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 True ，否则请返回 False 。

 

示例 1：

输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
示例 2：

输入：s = "00110", k = 2
输出：true
示例 3：

输入：s = "0110", k = 1
输出：true
解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
示例 4：

输入：s = "0110", k = 2
输出：false
解释：长度为 2 的二进制串 "00" 没有出现在 s 中。
示例 5：

输入：s = "0000000001011100", k = 4
输出：false
 

提示：

1 <= s.length <= 5 * 10^5
s 中只含 0 和 1 。
1 <= k <= 20

"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        def getKStr(k):
            if k ==0:
                return [""]
            coll = getKStr(k-1)
            res = []
            for s in coll:
                res.append(s+'0')
                res.append(s+'1')
            return res
        for p in getKStr(k):
            if p not in s:
                return False
        return True


s =Solution()
s.hasAllCodes("",2)