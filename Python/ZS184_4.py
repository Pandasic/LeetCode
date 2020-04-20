"""
5383. 给 N x 3 网格图涂色的方案数 显示英文描述 
用户通过次数36
用户尝试次数41
通过次数36
提交次数46
题目难度Hard
你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。

给你网格图的行数 n 。

请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。

 

示例 1：

输入：n = 1
输出：12
解释：总共有 12 种可行的方法：

示例 2：

输入：n = 2
输出：54
示例 3：

输入：n = 3
输出：246
示例 4：

输入：n = 7
输出：106494
示例 5：

输入：n = 5000
输出：30228214
 

提示：

n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""
"""
JAVA
public class Solution {
    public int NumOfWays(int n) {
            if (n == 0)
                return 0;
            else if (n == 1)
                return 12;
            var temp = 1000000007;
            long  repeat = 6;
            long  unrepeat = 6;
            for(int i = 2; i <=n; i++)
            {
                long  newrep = (repeat * 3) % temp + unrepeat * 2 % temp;
                long  newunrep = repeat * 2 % temp + unrepeat * 2 % temp;
                repeat = newrep;
                unrepeat = newunrep;
            }
            return (int)((repeat + unrepeat)%temp);
    }
}

作者：LindsayWong
链接：https://leetcode-cn.com/problems/number-of-ways-to-paint-n-x-3-grid/solution/shu-xue-jie-jue-fei-chang-kuai-le-by-lindsaywong/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""