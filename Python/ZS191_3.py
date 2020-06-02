"""
426. 重新规划路线 显示英文描述 
通过的用户数229
尝试过的用户数269
用户总通过次数229
用户总提交次数293
题目难度Medium
n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。

路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。

今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。

请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。

题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。

 

示例 1：



输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
示例 2：



输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
示例 3：

输入：n = 3, connections = [[1,0],[2,0]]
输出：0
 

提示：

2 <= n <= 5 * 10^4
connections.length == n-1
connections[i].length == 2
0 <= connections[i][0], connections[i][1] <= n-1
connections[i][0] != connections[i][1]
"""
#超时
class Solution_old:
    def minReorder(self, n, connections):
        q = [0]
        res = 0
        while(len(q) > 0):
            rmb = []
            v = q.pop(0)
            for i in range(len(connections)):
                if v in connections[i]:
                    rmb.append(connections[i])
                    if connections[i][0] == v:
                        res +=1
                        q.append(connections[i][1])
                    else:
                        q.append(connections[i][0])
            for b in rmb:
                connections.remove(b)
        return res

class Solution:
    #广度优先搜索
    def minReorder(self, n, connections):

        #in out
        M = [[[],[]] for i in range(n)]
        for c in connections:
            M[c[0]][1].append(c[1])
            M[c[1]][0].append(c[0])

        q = [(0,None)]
        recode = set()
        res = 0
        while(len(q) > 0):
            v,f = q.pop(0)
            recode.add(v)
            res += len(M[v][1])
            for i in M[v][0] + M[v][1]:
                if i not in recode:
                    q.append((i,v))

        return res

s  =Solution()
s.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]])