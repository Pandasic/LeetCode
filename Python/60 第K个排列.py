"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

"""
import math
class Solution:
    def getPermutation(self, n: int, k: int):
        k = k - 1
        nums = [i for i in range(1,n+1)]
        res = []
        for i in range(n):
            #print(nums[k//math.factorial(n-1)])
            res.append(nums[k//math.factorial(n - 1)])
            del nums[k//math.factorial(n-1)]
            print(nums)
            k = k % math.factorial(n-1)
            n -= 1
        return "".join([str(r) for r in res])

s = Solution()
n = 4
print(s.getPermutation(1,1))

for i in range(9):
    print(math.factorial(i))