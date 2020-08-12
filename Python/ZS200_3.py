"""
5477. 排布二进制网格的最少交换次数 显示英文描述 
通过的用户数877
尝试过的用户数1430
用户总通过次数886
用户总提交次数2797
题目难度Medium
给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。

一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。

请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。

主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。

 

示例 1：



输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
输出：3
示例 2：



输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
输出：-1
解释：所有行都是一样的，交换相邻行无法使网格符合要求。
示例 3：



输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
输出：0
 

提示：

n == grid.length
n == grid[i].length
1 <= n <= 200
grid[i][j] 要么是 0 要么是 1 。

"""
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        arr = []
        n = len(grid)
        if n<= 0:
            return 0
        
        for i in range(n):
            z = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 0:
                    z +=1
                else:
                    break
            arr.append(z)
        res = 0
        for i in range(n):
            require =  n - i - 1
            aim = 0
            for j in range(i,n):
                if arr[j] >= require:
                    aim = j
                    break
            else:
                return -1
            
            for j in range(aim,i,-1):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                res += 1
                
            #print(arr,aim,i,require)
        return res
            