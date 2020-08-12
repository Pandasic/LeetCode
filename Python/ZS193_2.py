"""
5437. 不同整数的最少数目 显示英文描述 
通过的用户数485
尝试过的用户数594
用户总通过次数485
用户总提交次数694
题目难度Medium
给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目。

 

示例 1：

输入：arr = [5,5,4], k = 1
输出：1
解释：移除 1 个 4 ，数组中只剩下 5 一种整数。
示例 2：

输入：arr = [4,3,1,1,3,3,2], k = 3
输出：2
解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。
 

提示：

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        m = {}
        for v in arr:
            if not v in m.keys():
                m[v] = 0
            m[v] += 1
        m = list(m.items())
        m.sort(key = lambda x:x[1])
        res = len(m)
        for num,count in m:
            if k - count >= 0:
                k -= count
                res -= 1
            else:
                break
        return res