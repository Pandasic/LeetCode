"""
5391. 生成数组 显示英文描述 
通过的用户数162
尝试过的用户数211
用户总通过次数176
用户总提交次数278
题目难度Hard
给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。

lnaximu value
lnaximum index
searLh c;ost ±

ch co5t ±
arr. length

ror (i

0;  { n; i++) -

ir (rmaxirmum_value c arr[i]) \
rmaxirmumvalue = arr[i]
rmaxirmum irdex = i
5earch cost ± searI;h cost

returrn maxirmulln inaex



请你生成一个具有下述属性的数组 arr ：

arr 中有 n 个整数。
1 <= arr[i] <= m 其中 (0 <= i < n) 。
将上面提到的算法应用于 arr ，search_cost 的值等于 k 。
返回上述条件下生成数组 arr 的 方法数 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。

 

示例 1：

输入：n = 2, m = 3, k = 1
输出：6
解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
示例 2：

输入：n = 5, m = 2, k = 3
输出：0
解释：没有数组可以满足上述条件
示例 3：

输入：n = 9, m = 1, k = 1
输出：1
解释：可能的数组只有 [1, 1, 1, 1, 1, 1, 1, 1, 1]
示例 4：

输入：n = 50, m = 100, k = 25
输出：34549172
解释：不要忘了对 1000000007 取余
示例 5：

输入：n = 37, m = 17, k = 7
输出：418930126
 

提示：

1 <= n <= 50
1 <= m <= 100
0 <= k <= n
"""

#寻找最大值和最大下表
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        def getMax(arr):
            maxVal = -1
            maxIndex = -1
            searchCost = 0
            n =len(arr)
            for i in range(n):
                if maxVal < arr[i]:
                    maxVal = arr[i]
                    maxIndex = i
                    searchCost += 1
            return maxIndex